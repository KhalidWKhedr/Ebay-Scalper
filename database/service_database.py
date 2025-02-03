from database.manager_mongo_connector import MongoConnectionManager
from logger.service_logging import LoggingService
from utils.manager_secure_config import SecureConfigManager


class DatabaseService:
    def __init__(self):
        self.db_connection = None
        self.config = SecureConfigManager(connection_details=None)

    def save_connection_settings(self, connection_details):
        """Save encrypted database connection details."""
        for key, value in connection_details.items():
            if value is not None:
                self.config.write(key, str(value))

    def get_connection_settings(self):
        """Retrieve and decrypt database connection details."""
        return self.config.get_all()

    def connect(self, connection_details):
        """Attempts to connect to MongoDB based on the provided details."""
        try:
            LoggingService.log(
                f"Attempting to connect to database: {connection_details.db_name} at {connection_details.host}:{connection_details.port}",
                level="info")

            mongo_manager = MongoConnectionManager(connection_details)
            self.db_connection = mongo_manager.connect()

            if not self.db_connection:
                LoggingService.log(
                    f"Could not connect to MongoDB at {connection_details.db_name}:{connection_details.port}",
                    level="error")
                return "Could not connect to MongoDB."

            LoggingService.log(
                f"Successfully connected to MongoDB at {connection_details.host}:{connection_details.port}",
                level="info")
            return "Connected to MongoDB!"

        except Exception as e:
            LoggingService.log(f"Error connecting to MongoDB: {str(e)}", level="error")
            return f"Error: {str(e)}"
