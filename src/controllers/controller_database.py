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
        try:
            message_connect = self.database_service.connect(connection_details)
            if message_connect == "Connection successful":
                self.notification_service.show_message(self, message_connect)
            else:
                self.notification_service.show_message(self, f"Error: {message_connect}")
        except Exception as e:
            self.notification_service.show_message(self, f"Error: {str(e)}")
