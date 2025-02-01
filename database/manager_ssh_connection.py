from socket import socket
from urllib.parse import quote

import paramiko
import pymongo
from sshtunnel import SSHTunnelForwarder
from logger import service_logging


class SSHConnectionManager:
    def __init__(self, connection_details):
        self.ssh_host = connection_details['ssh_host']
        self.ssh_port = connection_details['ssh_port']
        self.ssh_username = quote(connection_details['ssh_username'])
        self.ssh_password = quote(connection_details['ssh_password'])
        self.mongo_host = connection_details['host']
        self.mongo_port = connection_details['port']
        self.mongo_user = connection_details['user']
        self.mongo_password = connection_details['password']
        self.db_name = connection_details['db_name']
        self.auth_source = connection_details['auth_source']
        self.uri = f"mongodb://{self.ssh_username}:{self.ssh_password}@localhost:27018/{self.db_name}?authSource={self.auth_source}&authMechanism=SCRAM-SHA-1"

        self.logger = service_logging.LoggingService.get_logger()

        self.tunnel = None
        self.client = None

    def _create_tunnel(self):
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
        """Connect to MongoDB via the SSH tunnel."""
        try:
            self._create_tunnel()

            if not self.tunnel.is_active:
                self.logger.error("SSH tunnel is not active. Aborting MongoDB connection.")
                return None

            escaped_user = quote(self.mongo_user)
            escaped_password = quote(self.mongo_password)
            print(self.uri)
            self.client = pymongo.MongoClient(self.uri, serverSelectionTimeoutMS=5000)

            self.client.admin.command("ping")

            self.logger.info(
                f"Successfully connected to MongoDB at {self.mongo_host}:{self.mongo_port}, database: {self.db_name} via SSH tunnel."
            )
            return self.client

        except paramiko.ssh_exception.AuthenticationException as auth_error:
            self.logger.error(
                f"SSH Authentication failed for {self.ssh_username}@{self.ssh_host}. Error: {repr(auth_error)}")
            if self.tunnel:
                self.tunnel.stop()
            return None

        except paramiko.ssh_exception.SSHException as ssh_error:
            self.logger.error(f"SSH connection failed to {self.ssh_host}:{self.ssh_port}. Error: {repr(ssh_error)}")
            if self.tunnel:
                self.tunnel.stop()
            return None

        except Exception as e:
            self.logger.error(f"Unexpected error occurred: {repr(e)}")
            if self.tunnel:
                self.tunnel.stop()
            return None

    def close(self):
        """Closes the SSH tunnel and MongoDB connection."""
        if self.client:
            self.client.close()
            self.logger.info("MongoDB connection closed.")
            self.client = None
        if self.tunnel and self.tunnel.is_active:
            self.tunnel.stop()
            self.logger.info("SSH tunnel closed.")
            self.tunnel = None
