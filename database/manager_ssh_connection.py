from urllib.parse import quote
import pymongo
from sshtunnel import SSHTunnelForwarder
from logger import service_logging


class SSHConnectionManager:
    def __init__(self, connection_details):
        self.ssh_host = connection_details['ssh_host']
        self.ssh_port = connection_details['ssh_port']
        self.ssh_username = connection_details['ssh_username']
        self.ssh_password = connection_details['ssh_password']
        self.mongo_host = connection_details['host']
        self.mongo_port = connection_details['port']
        self.mongo_user = connection_details['user']
        self.mongo_password = connection_details['password']
        self.db_name = connection_details['db_name']
        self.auth_source = connection_details['auth_source']
        self.logger = service_logging.LoggingService.get_logger()

        self.tunnel = None
        self.client = None

    def connect(self):
        """Handles the SSH connection and MongoDB tunnel setup."""
        try:
            self.tunnel = SSHTunnelForwarder(
                (self.ssh_host, self.ssh_port),
                ssh_username=self.ssh_username,
                ssh_password=self.ssh_password,
                remote_bind_address=(self.mongo_host, self.mongo_port),
                local_bind_address=("localhost", 27018)
            )
            self.tunnel.start()

            local_port = self.tunnel.local_bind_port
            self.logger.info(f"Successfully established SSH tunnel to {self.ssh_host}:{self.ssh_port}, forwarding to local port {local_port}.")

            escaped_user = quote(self.mongo_user)
            escaped_password = quote(self.mongo_password)
            uri = f"mongodb://{escaped_user}:{escaped_password}@localhost:27018/{self.db_name}?authSource={self.auth_source}&authMechanism=SCRAM-SHA-1"
            print(uri)
            self.client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
            self.client.admin.command("ping")

            self.logger.info(f"Successfully connected to MongoDB at {self.mongo_host}:{self.mongo_port}, database: {self.db_name} via SSH tunnel.")
            return self.client

        except Exception as e:
            self.logger.error(
                f"Failed to connect via SSH to {self.ssh_host}:{self.ssh_port} or MongoDB at {self.mongo_host}:{self.mongo_port}. Error: {repr(e)}"
            )
            self.close()
            return None

    def close(self):
        """Closes the SSH tunnel and MongoDB connection."""
        if self.client:
            self.client.close()
            self.logger.info("MongoDB connection closed.")
            self.client = None
        if self.tunnel:
            self.tunnel.stop()
            self.logger.info("SSH tunnel closed.")
            self.tunnel = None
