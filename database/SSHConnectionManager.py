from urllib.parse import quote
import pymongo
from sshtunnel import SSHTunnelForwarder
from logger import LoggingService  # Update to reflect your actual import path for LoggingService


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
        self.logger = LoggingService.LoggingService.get_logger()

    def connect(self):
        """Handles the SSH connection and the tunnel setup."""
        try:
            with SSHTunnelForwarder(
                    (self.ssh_host, self.ssh_port),
                    ssh_username=self.ssh_username,
                    ssh_password=self.ssh_password,
                    remote_bind_address=(self.mongo_host, self.mongo_port)) as tunnel:

                self.logger.info(f"Successfully established SSH tunnel to {self.ssh_host}:{self.ssh_port}.")

                escaped_user = quote(self.mongo_user)
                escaped_password = quote(self.mongo_password)
                uri = f"mongodb://{escaped_user}:{escaped_password}@127.0.0.1:{tunnel.local_bind_port}/{self.db_name}?authSource={self.auth_source}"
                client = pymongo.MongoClient(uri)

                self.logger.info(
                    f"Successfully connected to MongoDB at {self.mongo_host}:{self.mongo_port}, database: {self.db_name} via SSH tunnel.")

                return True

        except Exception as e:
            # Log the exception in case of an error
            self.logger.error(
                f"Failed to connect via SSH to {self.ssh_host}:{self.ssh_port} or MongoDB at {self.mongo_host}:{self.mongo_port}. Error: {str(e)}")
            return False
