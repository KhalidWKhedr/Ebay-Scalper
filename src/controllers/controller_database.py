from src.services.service_database import DatabaseService
from logger.service_logging import LoggingService
from src.models.model_database_connection_details import SchemaConnectionDetails
from src.services.service_notification import NotificationService
from utils.converter import Converter


class DatabaseController:
    def __init__(self, database_service: DatabaseService, logger: LoggingService,
                 converter: Converter, notification_service: NotificationService,
                 schema_connection_details: SchemaConnectionDetails):
        self.logger = logger
        self.converter = converter
        self.database_service = database_service
        self.notification_service = notification_service
        self.schema_connection_details = schema_connection_details

    def get_connection_settings(self):
        """Retrieve connection settings from the database service."""
        return self.database_service.get_connection_settings()

    def save_connection_settings(self, connection_details: SchemaConnectionDetails):
        """Save connection settings using the database service."""
        return self.database_service.save_connection_settings(connection_details)

    def connect_to_db(self, connection_details: SchemaConnectionDetails):
        """Attempt to connect to the database."""
        self.logger.log(f"Attempting to connect to database at host: {connection_details.host}", level="info")

        try:
            message_connection = self.database_service.connect(connection_details)
            message_save = self.save_connection_settings(connection_details)
            self.logger.log(f"Connection successful: {message_connection}", level="info")
            self.logger.log(f"Saved details: {message_save}", level="info")
            return message_connection
        except ConnectionError as e:
            error_message = f"Database connection error: {str(e)}"
            self.logger.log(error_message, level="error")
            raise ConnectionError(error_message)
        except Exception as e:
            error_message = f"Unexpected error: {str(e)}"
            self.logger.log(error_message, level="critical")
            raise Exception(error_message)