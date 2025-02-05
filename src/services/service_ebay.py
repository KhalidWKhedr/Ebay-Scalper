from logger.service_logging import LoggingService
from src.ebay.manager_ebay_connection import EbayConnectionManager
from utils.manager_secure_config import SecureConfigManager

class EbayService:
    def __init__(
        self,
        logger: LoggingService,
        secure_config: SecureConfigManager
        ):

        self.logger = logger
        self.secure_config = secure_config
        self.ebay_connection_manager = None
        self.ebay_connection = None

    @staticmethod
    def check_app_id(connection_details):
        if not connection_details['API_ID']:
            raise ValueError("Missing required environment variable APP_ID.")

    def save_ebay_connection_settings(self, connection_details):
        """Save eBay connection settings."""
        for key, value in connection_details.items():
            if value is not None:
                self.secure_config.write(key, str(value))

    def connect(self, connection_details):
        try:

            self.logger.get_logger().info(f"Attempting to connect to eBay API: {connection_details}")
            self.check_app_id(connection_details)
            if not self.ebay_connection_manager:
                self.ebay_connection_manager = EbayConnectionManager(connection_details)

            self.save_ebay_connection_settings(connection_details)
            api = self.ebay_connection_manager.connect_to_ebay()

            if not api:
                self.logger.get_logger().error(
                    f"Could not connect to eBay API at {connection_details.get('API_DOMAIN')}")
                return "Could not connect to eBay API."

            self.logger.get_logger().info(
                f"Successfully connected to eBay API at {connection_details.get('API_DOMAIN')}")
            return "Connected to eBay API!"

        except Exception as e:
            self.logger.get_logger().error(f"Error connecting to eBay API: {str(e)}")
            return f"Error: {str(e)}"