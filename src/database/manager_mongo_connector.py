from urllib.parse import quote
from typing import Optional, Dict, Any
import pymongo
from sshtunnel import SSHTunnelForwarder
from utils.manager_secure_config import SecureConfigManager


class MongoConnectionManager:
    def __init__(self, secure_config_manager: SecureConfigManager):
        self.secure_config_manager = secure_config_manager
        self.tunnel: Optional[SSHTunnelForwarder] = None
        self.client: Optional[pymongo.MongoClient] = None

    def _create_ssh_tunnel(self, ssh_config: Dict[str, Any], mongo_host: str, mongo_port: int) -> int:
        """Create an SSH tunnel for MongoDB connection."""
        try:
            self.tunnel = SSHTunnelForwarder(
                (ssh_config["SSH_HOST"], int(ssh_config["SSH_PORT"])),
                ssh_username=ssh_config["SSH_USERNAME"],
                ssh_password=ssh_config["SSH_PASSWORD"],
                remote_bind_address=(mongo_host, mongo_port),
                local_bind_address=("localhost", 27018)
            )
            self.tunnel.start()
            print("SSH tunnel created successfully.")
            return self.tunnel.local_bind_port
        except Exception as e:
            raise Exception(f"Failed to create SSH tunnel: {repr(e)}")

    def _build_mongo_uri(self, mongo_config: Dict[str, Any], local_port: int) -> str:
        """Build the MongoDB connection URI."""
        mongo_user = quote(mongo_config["MONGO_USER"])
        mongo_password = quote(mongo_config["MONGO_PASSWORD"])
        mongo_db_name = mongo_config["MONGO_DB_NAME"]
        mongo_auth_db = mongo_config["MONGO_AUTH_DB"]

        return (
            f"mongodb://{mongo_user}:{mongo_password}@localhost:{local_port}/"
            f"{mongo_db_name}?authSource={mongo_auth_db}"
        )

    def _validate_connection_details(self, mongo_config: Dict[str, Any]) -> None:
        """Validate required MongoDB connection details."""
        required_fields = ["MONGO_HOST", "MONGO_PORT", "MONGO_USER", "MONGO_PASSWORD", "MONGO_DB_NAME"]
        for field in required_fields:
            if not mongo_config.get(field):
                raise ValueError(f"Missing required connection detail: {field}")

    def connect(self) -> pymongo.MongoClient:
        """Connect to MongoDB, either directly or via an SSH tunnel."""
        try:

            mongo_config = {
                "MONGO_HOST": self.secure_config_manager.read("MONGO_HOST"),
                "MONGO_PORT": int(self.secure_config_manager.read("MONGO_PORT")),
                "MONGO_USER": self.secure_config_manager.read("MONGO_USER"),
                "MONGO_PASSWORD": self.secure_config_manager.read("MONGO_PASSWORD"),
                "MONGO_AUTH_DB": self.secure_config_manager.read("MONGO_AUTH_DB"),
                "MONGO_DB_NAME": self.secure_config_manager.read("MONGO_DB_NAME"),
            }

            ssh_config = {
                "SSH_TOGGLE": self.secure_config_manager.read("SSH_TOGGLE") == "True",
                "SSH_HOST": self.secure_config_manager.read("SSH_HOST"),
                "SSH_PORT": self.secure_config_manager.read("SSH_PORT"),
                "SSH_USERNAME": self.secure_config_manager.read("SSH_USERNAME"),
                "SSH_PASSWORD": self.secure_config_manager.read("SSH_PASSWORD"),
            }

            self._validate_connection_details(mongo_config)

            local_port = 27018
            if ssh_config["SSH_TOGGLE"]:
                local_port = self._create_ssh_tunnel(ssh_config, mongo_config["MONGO_HOST"], mongo_config["MONGO_PORT"])

            uri = self._build_mongo_uri(mongo_config, local_port)
            self.client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
            self.client.admin.command("ping")  # Test the connection
            print("Connected to MongoDB successfully.")
            return self.client
        except Exception as e:
            raise Exception(f"Failed to connect to MongoDB: {repr(e)}")

    def close(self) -> None:
        """Close the MongoDB connection and SSH tunnel (if active)."""
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")
        if self.tunnel and self.tunnel.is_active:
            self.tunnel.stop()
            print("SSH tunnel closed.")