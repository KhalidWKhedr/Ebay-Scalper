from logger.service_logging import LoggingService
from src.ebay.manager_ebay_connection import EbayConnectionManager
from utils.manager_secure_config import SecureConfigManager
from typing import Dict, Optional


class EbayService:
    def __init__(
        self,
        logger: LoggingService,
        secure_config: SecureConfigManager,
        ebay_connection_manager: Optional[EbayConnectionManager] = None
    ):
        self.logger = logger
        self.secure_config = secure_config
        self.ebay_connection_manager = ebay_connection_manager

    @staticmethod
    def check_app_id(connection_details: Dict[str, str]):
        """Check if API_ID is present in connection details."""
        if not connection_details.get('API_ID'):
            raise ValueError("Missing required environment variable API_ID.")

    def save_ebay_connection_settings(self, connection_details: Dict[str, str]):
        """Save eBay connection settings securely."""
        for key, value in connection_details.items():
            if value is not None:
                self.secure_config.write(key, str(value))

    def connect(self, connection_details: Dict[str, str]) -> str:
        """Connect to the eBay API using the provided connection details."""
        try:
            # Log attempt to connect
            self.logger.get_logger().info(f"Attempting to connect to eBay API with details: {connection_details}")

            # Check for the presence of API_ID
            self.check_app_id(connection_details)

            # Initialize EbayConnectionManager if it is not already initialized
            if not self.ebay_connection_manager:
                self.ebay_connection_manager = EbayConnectionManager(api_details=connection_details, logger=self.logger)

            # Save connection settings securely
            self.save_ebay_connection_settings(connection_details)

            # Attempt to connect to eBay API
            api = self.ebay_connection_manager.connect_to_ebay()

            if not api:
                return self._handle_error(connection_details, "Could not connect to eBay API")

            # Log success
            success_message = f"Successfully connected to eBay API at {connection_details.get('API_DOMAIN')}"
            self.logger.get_logger().info(success_message)
            return success_message

        except ValueError as ve:
            return self._handle_error(connection_details, f"ValueError: {str(ve)}")

        except Exception as e:
            return self._handle_error(connection_details, f"Error connecting to eBay API: {str(e)}")

    def _handle_error(self, connection_details: Dict[str, str], error_message: str) -> str:
        """Helper method to handle errors and log them."""
        self.logger.get_logger().error(f"{error_message} at {connection_details.get('API_DOMAIN')}")
        return error_message
