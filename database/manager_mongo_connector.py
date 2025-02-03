from urllib.parse import quote

import pymongo
from sshtunnel import SSHTunnelForwarder


class MongoConnectionManager:
    def __init__(self, connection_details):
        # Access connection details using dot notation (assuming SchemaConnectionDetails object)
        self.ssh_checked = connection_details.use_ssh
        self.ssh_host = connection_details.ssh_host if self.ssh_checked else None
        self.ssh_port = connection_details.ssh_port if self.ssh_checked else None
        self.ssh_username = connection_details.ssh_username if self.ssh_checked else None
        self.ssh_password = connection_details.ssh_password if self.ssh_checked else None
        self.mongo_host = connection_details.host
        self.mongo_port = connection_details.port
        self.mongo_user = connection_details.user
        self.mongo_password = connection_details.password
        self.db_name = connection_details.db_name
        self.auth_source = connection_details.auth_source
        self.auth_type = connection_details.auth_type
        self.uri = f"mongodb://{quote(self.mongo_user)}:{quote(self.mongo_password)}@localhost:27018/{self.db_name}?authSource={self.auth_source}&authMechanism={self.auth_type}"

        # Additional initialization
        self.tunnel = None
        self.client = None
        print(connection_details)

    def _create_tunnel(self):
        """Creates the SSH tunnel."""
        if self.ssh_checked:
            try:
                self.tunnel = SSHTunnelForwarder(
                    (self.ssh_host, self.ssh_port),
                    ssh_username=self.ssh_username,
                    ssh_password=self.ssh_password,
                    remote_bind_address=(self.mongo_host, self.mongo_port),
                    local_bind_address=(self.mongo_host, 27018)
                )
                self.tunnel.start()
                local_port = self.tunnel.local_bind_port
                return local_port
            except Exception as e:
                raise Exception(f"Failed to create SSH tunnel: {repr(e)}")

    def connect(self):
        """Connect to MongoDB, either via SSH tunnel or directly."""
        try:

            if self.ssh_checked:
                local_port = self._create_tunnel()
                self.uri = self.uri.replace("localhost:27018", f"localhost:{local_port}")

            self.client = pymongo.MongoClient(self.uri, serverSelectionTimeoutMS=5000)
            self.client.admin.command("ping")
            return self.client
        except Exception as e:
            raise Exception(f"Failed to connect to MongoDB: {repr(e)}")

    def close(self):
        """Closes the MongoDB connection and SSH tunnel (if active)."""
        if self.client:
            self.client.close()
        if self.tunnel and self.tunnel.is_active:
            self.tunnel.stop()
