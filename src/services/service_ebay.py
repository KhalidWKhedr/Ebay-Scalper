from src.ebay.manager_ebay_connection import EbayConnectionManager
from logger.service_logging import LoggingService

class EbayService:
    def __init__(self):
        self.ebay_connection = None

    def connect(self, connection_details):
        """Attempts to connect to eBay API based on the provided details."""
        try:
            LoggingService.log(
                f"Attempting to connect to eBay API: {connection_details['api_id']} at {connection_details['api_domain']}:{connection_details['api_site_id']}",
                level="info"
            )

            self.ebay_connection = EbayConnectionManager(connection_details)  # FIXED
            api = self.ebay_connection.connect_to_ebay()

            if not api:
                LoggingService.log(
                    f"Could not connect to eBay API at {connection_details['api_domain']}",
                    level="error"
                )
                return "Could not connect to eBay API."

            LoggingService.log(
                f"Successfully connected to eBay API at {connection_details['api_domain']}",
                level="info"
            )
            return "Connected to eBay API!"

        except Exception as e:
            LoggingService.log(f"Error connecting to eBay API: {str(e)}", level="error")
            return f"Error: {str(e)}"
