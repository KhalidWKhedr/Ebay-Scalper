from src.services.service_database import DatabaseService
from logger.service_logging import LoggingService
from src.models.model_database_connection_details import SchemaConnectionDetails
from src.services.service_notification import NotificationService
from utils.converter import Converter


class DatabaseController:
    def __init__(
        self,
        database_service: DatabaseService,
        logger: LoggingService,
        converter: Converter,
        notification_service: NotificationService,
    ):
        self.logger = logger
        self.converter = converter
        self.database_service = database_service
        self.notification_service = notification_service

    def get_connection_settings(self):
        """Retrieve connection settings from the database service."""
        return self.database_service.get_connection_settings()

    def save_connection_settings(self, connection_details: SchemaConnectionDetails):
        """Save connection settings using the database service."""
        return self.database_service.save_connection_settings(connection_details)

    def connect_to_db(self, connection_details: SchemaConnectionDetails) -> str:
        """Attempt to connect to the database and return a status message."""
        try:
            message_connect = self.database_service.connect(connection_details)

            if message_connect == "Connection successful":
                self.logger.log("Database connection successful.", level="info")
                return "Connection successful"
            else:
                error_message = f"Unexpected response from database service: {message_connect}"
                self.logger.log(error_message, level="error")
                return error_message

        except Exception as e:
            error_message = f"Failed to connect to the database: {str(e)}"
            self.logger.log(error_message, level="error")
            return error_message
