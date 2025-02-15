from src.models.model_database_connection_details import SchemaConnectionDetails
from src.database.manager_mongo_connector import MongoConnectionManager
from src.logger.service_logging import LoggingService
from src.utils.utils_manager_secure_config import SecureConfigManager

class DatabaseService:
    def __init__(
        self,
        logger: LoggingService,
        secure_config: SecureConfigManager,
        mongo_manager: MongoConnectionManager
    ):
        self.logger = logger
        self.secure_config = secure_config
        self.mongo_manager = mongo_manager
        self.db_connection = None

    def save_connection_settings(self, connection_details: SchemaConnectionDetails):
        """Save encrypted database connection details."""
        parsed_connection_details = connection_details.model_dump()
        for key, value in parsed_connection_details.items():
            if value is not None:
                self.secure_config.write(key, str(value))

    def get_connection_settings(self):
        """Retrieve and decrypt database connection details."""
        return self.secure_config.get_all()

    def connect(self, connection_details: SchemaConnectionDetails) -> str:
        """Attempts to connect to MongoDB based on the loaded details from secure config."""
        try:
            # Save connection details securely
            self.save_connection_settings(connection_details)
            connection_details = self.secure_config.get_all()

            # Ensure required keys are present in connection details
            required_keys = ["MONGO_HOST", "MONGO_PORT", "MONGO_DB_NAME", "MONGO_USER", "MONGO_PASSWORD"]
            if not all(key in connection_details for key in required_keys):
                error_message = "Missing required connection details in .env file."
                self.logger.log(error_message, level="error")
                raise ValueError(error_message)

            # Log the attempt to connect
            self.logger.log(
                f"Attempting to connect to database: {connection_details['MONGO_DB_NAME']} "
                f"at {connection_details['MONGO_HOST']}:{connection_details['MONGO_PORT']}",
                level="info"
            )

            # Ensure mongo_manager is provided
            if not self.mongo_manager:
                error_message = "MongoConnectionManager is not provided or initialized."
                self.logger.log(error_message, level="error")
                raise ValueError(error_message)

            # Establish the connection
            self.db_connection = self.mongo_manager.connect()

            # Log successful connection
            self.logger.log(f"Connection successful to {connection_details['MONGO_HOST']}", level="info")
            return "Connection successful"

        except ValueError as ve:
            # Handle specific ValueError exceptions (e.g., missing required keys or missing mongo manager)
            self.logger.log(f"ValueError: {str(ve)}", level="error")
            raise

        except Exception as e:
            # Handle other unexpected errors with context
            error_message = f"Database connection error: {str(e)}"
            self.logger.log(error_message, level="error")
            raise Exception(error_message)
