from urllib.parse import quote
import pymongo
from sshtunnel import SSHTunnelForwarder
from utils.manager_secure_config import SecureConfigManager

class MongoConnectionManager:
    def __init__(self, secure_config_manager: SecureConfigManager):
        self.secure_config_manager = secure_config_manager
        self.tunnel = None
        self.client = None

    def _create_tunnel(self, connection_details):
        """Creates the SSH tunnel if required."""
        if connection_details.get("SSH_TOGGLE", False):
            try:
                self.tunnel = SSHTunnelForwarder(
                    (connection_details["SSH_HOST"], int(connection_details["SSH_PORT"])),
                    ssh_username=connection_details["SSH_USERNAME"],
                    ssh_password=connection_details["SSH_PASSWORD"],
                    remote_bind_address=(connection_details["MONGO_HOST"], int(connection_details["MONGO_PORT"])),
                    local_bind_address=(connection_details["MONGO_HOST"], 27018)  # Bind to localhost
                )
                print("SSH tunnel created")
                self.tunnel.start()
                return self.tunnel.local_bind_port
            except Exception as e:
                raise Exception(f"Failed to create SSH tunnel: {repr(e)}")

    def connect(self):
        """Connect to MongoDB, either via SSH tunnel or directly."""
        try:
            mongo_host = self.secure_config_manager.read("MONGO_HOST")
            mongo_port = self.secure_config_manager.read("MONGO_PORT")
            mongo_user = self.secure_config_manager.read("MONGO_USER")
            mongo_password = self.secure_config_manager.read("MONGO_PASSWORD")
            mongo_auth_db = self.secure_config_manager.read("MONGO_AUTH_DB")
            mongo_db_name = self.secure_config_manager.read("MONGO_DB_NAME")
            ssh_toggle = self.secure_config_manager.read("SSH_TOGGLE") == "True"  # Updated for SSH_TOGGLE
            ssh_host = self.secure_config_manager.read("SSH_HOST")
            ssh_port = self.secure_config_manager.read("SSH_PORT")
            ssh_username = self.secure_config_manager.read("SSH_USERNAME")
            ssh_password = self.secure_config_manager.read("SSH_PASSWORD")
            auth_type = self.secure_config_manager.read("AUTH_TYPE")

            if not all([mongo_host, mongo_port, mongo_db_name, mongo_user, mongo_password]):
                raise ValueError("Missing required connection details in .env file")

            connection_details = {
                "mongo_host": mongo_host,
                "mongo_port": int(mongo_port),
                "mongo_user": mongo_user,
                "mongo_password": mongo_password,
                "mongo_auth_db": mongo_auth_db,
                "mongo_db_name": mongo_db_name,
                "ssh_toggle": ssh_toggle,
                "ssh_host": ssh_host,
                "ssh_port": ssh_port,
                "ssh_username": ssh_username,
                "ssh_password": ssh_password,
                "auth_type": auth_type,
            }

            local_port = 27018
            if ssh_toggle:
                local_port = self._create_tunnel(connection_details)

            uri = f"mongodb://{quote(mongo_user)}:{quote(mongo_password)}@localhost:{local_port}/{mongo_db_name}?authSource={mongo_auth_db}"

            self.client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
            self.client.admin.command("ping")
            print(self.client)
            return self.client
        except Exception as e:
            raise Exception(f"Failed to connect to MongoDB: {repr(e)}")

    def close(self):
        """Closes the MongoDB connection and SSH tunnel (if active)."""
        if self.client:
            self.client.close()
        if self.tunnel and self.tunnel.is_active:
            self.tunnel.stop()
