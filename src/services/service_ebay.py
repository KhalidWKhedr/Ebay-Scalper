from src.ebay.manager_ebay_connection import EbayConnectionManager
from logger.service_logging import LoggingService

class EbayService:
    def __init__(self, ebay_connection_manager: EbayConnectionManager, logger: LoggingService):
        self.logger = logger
        self.ebay_connection_manager = ebay_connection_manager
        self.ebay_connection = None

    def connect(self, connection_details):
        """Attempts to connect to eBay API based on the provided details."""
        try:
            self.logger.get_logger().info(
                f"Attempting to connect to eBay API: {connection_details['api_id']} "
                f"at {connection_details['api_domain']}:{connection_details['api_site_id']}"
            )

            api = self.ebay_connection.connect_to_ebay()

            if not api:
                self.logger.get_logger().error(
                    f"Could not connect to eBay API at {connection_details['api_domain']}"
                )
                return "Could not connect to eBay API."

            self.logger.get_logger().info(
                f"Successfully connected to eBay API at {connection_details['api_domain']}"
            )
            return "Connected to eBay API!"

        except Exception as e:
            self.logger.get_logger().error(f"Error connecting to eBay API: {str(e)}")
            return f"Error: {str(e)}"
