from src.services.service_database import DatabaseService
from src.logger.service_logging import LoggingService
from src.models.model_database_connection_details import SchemaConnectionDetails
from src.utils.utils_converter import Converter
import traceback


class DatabaseController:
    def __init__(
        self,
        logger: LoggingService,
        database_service: DatabaseService,
        converter: Converter
    ):
        """
        Initialize the DatabaseController with the provided services.

        :param database_service: Service responsible for database interactions.
        :param logger: Logger for recording events and errors.
        :param converter: Service responsible for data conversion.
        """
        self.logger = logger
        self.converter = converter
        self.database_service = database_service

    def get_connection_settings(self):
        """
        Retrieve the current database connection settings from the database service.

        :return: The connection settings.
        """
        return self.database_service.get_connection_settings()

    def save_connection_settings(self, connection_details: SchemaConnectionDetails):
        """
        Save new connection settings to the database.

        :param connection_details: The connection details to be saved.
        :return: The result of the save operation.
        """
        return self.database_service.save_connection_settings(connection_details)

    def connect_to_db(self, connection_details: SchemaConnectionDetails) -> str:
        """Attempts to connect and logs the result."""
        success = self.database_service.connect(connection_details)

        if success:
            self.logger.get_logger().info("Database connection successful.")
        else:
            self.logger.error("Database connection failed.")

        return success
