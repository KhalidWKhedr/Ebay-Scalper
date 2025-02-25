from src.logger.service_logging import LoggingService
from src.infrastructure.external.connector_ebay import ConnectorEbay
from src.utils.utils_manager_secure_config import SecureConfigManager
from typing import Dict, Optional


class EbayService:
    def __init__(
        self,
        logger: LoggingService,
        secure_config: SecureConfigManager,
        connector_ebay: Optional[ConnectorEbay] = None
    ):
        self.logger = logger
        self.secure_config = secure_config
        self.connector_ebay = connector_ebay or ConnectorEbay(logger=self.logger)

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

    def get_saved_ebay_connection_settings(self):
        """Retrieve and decrypt eBay API settings."""
        return self.secure_config.get_all()

    def initialize_api(self, connection_details: Dict[str, str]):
        """Initialize eBay API client with given connection details."""
        self.logger.get_logger().info(f"Initializing eBay API with domain: {connection_details.get('API_DOMAIN')}")
        self.check_app_id(connection_details)
        return self.connector_ebay.connect_to_ebay(connection_details)

    def test_connection(self, connection_details: Dict[str, str]) -> str:
        """Test API connection by making a minimal query."""
        try:
            api = self.initialize_api(connection_details)

            if not api:
                return self._handle_error(connection_details, "Test connection failed: Could not connect to eBay API.")

            # Perform a simple fetch request to validate connection
            test_response = api.execute("findItemsAdvanced", {"keywords": "test"}).dict()

            if test_response.get("ack") == "Success":
                items = test_response.get("searchResult", {}).get("item", [])
                print(items)
                return f"Test connection successful for {connection_details.get('API_DOMAIN')}."

            return self._handle_error(connection_details, f"Test API request failed: {test_response}")

        except ValueError as ve:
            return self._handle_error(connection_details, f"ValueError: {str(ve)}")

        except Exception as e:
            return self._handle_error(connection_details, f"Error during test connection: {str(e)}")

    def scrape_and_store(self, connection_details: Dict[str, str], query=None):
        """Fetch eBay data using a validated connection."""
        try:
            api = self.initialize_api(connection_details)

            if not api:
                return self._handle_error(connection_details, "Failed to initialize API connection.")

            response = api.execute("findItemsAdvanced", {"keywords": query}).dict()

            if response.get("ack") == "Success":
                items = response.get("searchResult", {}).get("item", [])

                if items:
                    self.logger.get_logger().info(f"Fetched {len(items)} items for query '{query}'.")
                    for item in items:
                        print(item)
                    return items  # Consider processing these further

                return self._handle_error(connection_details, f"No items found for query '{query}'.")

            return self._handle_error(connection_details, f"API call failed for '{query}'. Response: {response}")

        except Exception as e:
            return self._handle_error(connection_details, f"Error scraping for '{query}': {e}")

    def _handle_error(self, connection_details: Dict[str, str], error_message: str) -> str:
        """Helper method to handle errors and log them."""
        self.logger.get_logger().error(f"{error_message} at {connection_details.get('API_DOMAIN')}")
        return error_message
