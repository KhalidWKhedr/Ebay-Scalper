from src.logger.service_logging import LoggingService
from src.services.service_ebay import EbayService
from src.models.model_site_domain_ebay import SiteDomainModel


class EbayController:
    def __init__(
        self,
        logger: LoggingService,
        ebay_service: EbayService,
        site_domain_model: SiteDomainModel
    ):
        """
        Initialize the EbayApiController with necessary services.

        :param ebay_service: Service responsible for handling eBay API interactions.
        :param logger: Logger for recording events and errors.
        :param site_domain_model: Model for handling site and domain data related to eBay.
        """
        self.logger = logger
        self.ebay_service = ebay_service
        self.site_domain_model = site_domain_model

    def save_connection_settings(self, api_details: dict[str, str]):
        """Save the current eBay API settings."""
        return self.ebay_service.save_ebay_connection_settings(api_details)

    def test_connection(self, api_details: dict) -> bool:
        """
        Handle the eBay API connection process.
        """
        try:
            self.logger.get_logger().info("Attempting to connect to eBay API...")
            message = self.ebay_service.test_connection(api_details)
            self.logger.get_logger().info(message)
            return True
        except Exception as e:
            self.logger.error(f"Failed to connect to eBay API: {str(e)}")
            return False

    def get_saved_connection_settings(self):
        """Retrieve the current eBay API settings."""
        return self.ebay_service.get_saved_ebay_connection_settings()