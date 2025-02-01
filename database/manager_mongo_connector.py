from urllib.parse import quote
import pymongo
import paramiko
from sshtunnel import SSHTunnelForwarder
from logger import service_logging


class MongoConnectionManager:
    def __init__(self, connection_details):
        self.ssh_checked = connection_details['use_ssh']
        self.ssh_host = connection_details.get('ssh_host', None)
        self.ssh_port = connection_details.get('ssh_port') if self.ssh_checked else None
        self.ssh_username = connection_details.get('ssh_username', None) if self.ssh_checked else None
        self.ssh_password = connection_details.get('ssh_password', None) if self.ssh_checked else None
        self.mongo_host = connection_details['host']
        self.mongo_port = connection_details['port']
        self.mongo_user = connection_details['user']
        self.mongo_password = connection_details['password']
        self.db_name = connection_details['db_name']
        self.auth_source = connection_details['auth_source']
        self.auth_type = connection_details['auth_type']
        self.uri = f"mongodb://{quote(self.mongo_user)}:{quote(self.mongo_password)}@localhost:27018/{self.db_name}?authSource={self.auth_source}&authMechanism=SCRAM-SHA-1"

        self.logger = service_logging.LoggingService.get_logger()

        self.tunnel = None
        self.client = None


    def _create_tunnel(self):
        """Creates the SSH tunnel."""
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
            self.logger.info(
                f"Successfully established SSH tunnel to {self.ssh_host}:{self.ssh_port}, forwarding to local port {local_port}.")

        except paramiko.ssh_exception.AuthenticationException as auth_error:
            self.logger.error(
                f"SSH Authentication failed for {self.ssh_username}@{self.ssh_host}. Error: {repr(auth_error)}")
        except paramiko.ssh_exception.SSHException as ssh_error:
            self.logger.error(f"SSH connection failed to {self.ssh_host}:{self.ssh_port}. Error: {repr(ssh_error)}")
        except Exception as e:
            self.logger.error(
                f"Failed to connect via SSH to {self.ssh_host}:{self.ssh_port} or MongoDB at {self.mongo_host}:{self.mongo_port}. Error: {repr(e)}")

    def connect(self):
        """Connect to MongoDB, either via SSH tunnel or directly."""
        try:
            if self.ssh_checked:
                self._create_tunnel()

                if not self.tunnel.is_active:
                    self.logger.error("SSH tunnel is not active. Aborting MongoDB connection.")
                    return None

                self.uri = f"mongodb://{quote(self.mongo_user)}:{quote(self.mongo_password)}@localhost:27018/{self.db_name}?authSource={self.auth_source}&authMechanism=SCRAM-SHA-1"
                print(self.uri, self.auth_type)
            self.client = pymongo.MongoClient(self.uri, serverSelectionTimeoutMS=5000)

            self.client.admin.command("ping")

            self.logger.info(
                f"Successfully connected to MongoDB at {self.mongo_host}:{self.mongo_port}, database: {self.db_name}")
            return self.client

        except Exception as e:
            self.logger.error(f"Failed to connect to MongoDB. Error: {repr(e)}")
            if self.tunnel:
                self.tunnel.stop()
            self.client = None
            return None

    def close(self):
        """Closes the MongoDB connection and SSH tunnel (if active)."""
        if self.client:
            self.client.close()
            self.logger.info("MongoDB connection closed.")
            self.client = None
        if self.tunnel and self.tunnel.is_active:
            self.tunnel.stop()
            self.logger.info("SSH tunnel closed.")
            self.tunnel = None
