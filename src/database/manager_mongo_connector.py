from urllib.parse import quote
from typing import Optional, Dict, Any
import pymongo.errors
from sshtunnel import SSHTunnelForwarder

from logger.service_logging import LoggingService
from utils.manager_secure_config import SecureConfigManager

class MongoConnectionManager:
    def __init__(
        self,
        logger: LoggingService,
        secure_config_manager: SecureConfigManager
    ):
        """
        Initialize MongoConnectionManager with logger and secure config manager.

        :param logger: Instance of LoggingService for logging actions.
        :param secure_config_manager: Instance of SecureConfigManager for reading secure config values.
        """
        self.logger = logger
        self.secure_config_manager = secure_config_manager
        self.tunnel: Optional[SSHTunnelForwarder] = None
        self.client: Optional[pymongo.MongoClient] = None

    @staticmethod
    def _validate_connection_details(mongo_config: Dict[str, Any]) -> None:
        """
        Validate the required MongoDB connection details are provided in the config.

        :param mongo_config: A dictionary containing MongoDB configuration settings.
        :raises ValueError: If any required connection details are missing.
        """
        required_fields = ["MONGO_HOST", "MONGO_PORT", "MONGO_USER", "MONGO_PASSWORD", "MONGO_DB_NAME"]
        for field in required_fields:
            if not mongo_config.get(field):
                raise ValueError(f"Missing required connection detail: {field}")

    @staticmethod
    def _build_mongo_uri(mongo_config: Dict[str, Any], local_port: int) -> str:
        """
        Build the MongoDB connection URI using provided configuration and local port.

        :param mongo_config: A dictionary containing MongoDB connection details.
        :param local_port: Local port (either default or via SSH tunnel).
        :return: A fully constructed MongoDB URI.
        """
        mongo_user = quote(mongo_config["MONGO_USER"])
        mongo_password = quote(mongo_config["MONGO_PASSWORD"])
        mongo_db_name = mongo_config["MONGO_DB_NAME"]
        mongo_auth_db = mongo_config.get("MONGO_AUTH_DB", "admin")

        return f"mongodb://{mongo_user}:{mongo_password}@localhost:{local_port}/{mongo_db_name}?authSource={mongo_auth_db}"

    def _create_ssh_tunnel(self, ssh_config: Dict[str, Any], mongo_host: str, mongo_port: int) -> int:
        """
        Create an SSH tunnel to the remote MongoDB server.

        :param ssh_config: Dictionary containing SSH configuration.
        :param mongo_host: Hostname of the MongoDB server.
        :param mongo_port: Port of the MongoDB server.
        :return: Local port for the SSH tunnel.
        :raises Exception: If the SSH tunnel cannot be established.
        """
        try:
            self.tunnel = SSHTunnelForwarder(
                (ssh_config["SSH_HOST"], int(ssh_config["SSH_PORT"])),
                ssh_username=ssh_config["SSH_USERNAME"],
                ssh_password=ssh_config["SSH_PASSWORD"],
                remote_bind_address=(mongo_host, mongo_port),
                local_bind_address=("localhost", 27018)  # Use a local bind address for the tunnel.
            )
            self.tunnel.start()
            self.logger.log("SSH tunnel created successfully.")
            return self.tunnel.local_bind_port
        except Exception as e:
            self.logger.get_logger().error(f"Failed to create SSH tunnel: {repr(e)}")
            raise

    def connect(self) -> pymongo.MongoClient:
        """
        Establish a connection to MongoDB, either directly or via SSH tunnel.

        :return: A pymongo MongoClient instance.
        :raises pymongo.errors.ConnectionFailure: If the MongoDB connection fails.
        :raises Exception: For any other unexpected errors.
        """
        try:
            # Read MongoDB and SSH connection details from secure config manager
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

            # Validate MongoDB connection details
            self._validate_connection_details(mongo_config)

            # Determine the local port to use for the connection (default or via SSH tunnel)
            local_port = mongo_config["MONGO_PORT"]
            if ssh_config["SSH_TOGGLE"]:
                local_port = self._create_ssh_tunnel(ssh_config, mongo_config["MONGO_HOST"], local_port)

            # Build the MongoDB connection URI and create the MongoClient
            uri = self._build_mongo_uri(mongo_config, local_port)
            self.client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)

            # Test the connection by pinging the MongoDB server
            self.client.admin.command("ping")
            self.logger.log("Connected to MongoDB successfully.")
            return self.client

        except pymongo.errors.ConnectionFailure as e:
            self.logger.get_logger().error("MongoDB connection failed: %s", repr(e))
            self.close()  # Ensure cleanup
            raise
        except Exception as e:
            self.logger.get_logger().error("Unexpected error during MongoDB connection: %s", repr(e))
            self.close()  # Ensure cleanup
            raise

    def close(self) -> None:
        """
        Close the MongoDB connection and SSH tunnel (if active).

        This method ensures that resources are properly cleaned up after the connection is no longer needed.
        """
        if self.client:
            self.client.close()
            self.logger.log("MongoDB connection closed.")
        if self.tunnel and self.tunnel.is_active:
            self.tunnel.stop()
            self.logger.log("SSH tunnel closed.")
