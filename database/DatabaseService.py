from database.NormalConnectionManager import NormalConnectionManager
from database.SSHConnectionManager import SSHConnectionManager
from logger.LoggingService import LoggingService


class DatabaseService:
    def __init__(self):
        self.db_connection = None

    def create_connection(self, connection_details):
        """Creates a connection based on whether SSH is used."""
        if connection_details['use_ssh']:
            LoggingService.log(
                f"Creating SSH connection to {connection_details['ssh_host']}:{connection_details['ssh_port']}",
                level="info")
            return SSHConnectionManager(connection_details)
        else:
            LoggingService.log(
                f"Creating normal connection to {connection_details['host']}:{connection_details['port']}",
                level="info")
            return NormalConnectionManager(connection_details)

    def connect(self, connection_details):
        """Attempts to connect to MongoDB based on the provided details."""
        try:

            LoggingService.log(
                f"Attempting to connect to database: {connection_details['db_name']} at {connection_details['host']}:{connection_details['port']}",
                level="info")

            self.db_connection = self.create_connection(connection_details)
            success = self.db_connection.connect()

            if not success:

                LoggingService.log(
                    f"Could not connect to MongoDB at {connection_details['host']}:{connection_details['port']}",
                    level="error")
                return "Could not connect to MongoDB."

            LoggingService.log(
                f"Successfully connected to MongoDB at {connection_details['host']}:{connection_details['port']}",
                level="info")
            return "Connected to MongoDB!"

        except Exception as e:
            LoggingService.log(f"Error connecting to MongoDB: {str(e)}", level="error")
            return f"Error: {str(e)}"
