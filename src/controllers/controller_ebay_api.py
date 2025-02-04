from logger.service_logging import LoggingService
from src.ebay.ebay_site_domain import SITE_DOMAIN_MAPPING
from src.services.service_ebay import EbayService
from src.services.service_notification import NotificationService


class EbayApiController:
    def __init__(self, ebay_service: EbayService, notification_service: NotificationService,
                 site_domain_mapping: dict = SITE_DOMAIN_MAPPING):
        self.ebay_service = ebay_service
        self.site_domain_mapping = site_domain_mapping
        self.notification_service = notification_service

    def get_site_code(self, site_name: str) -> str:
        """Retrieve eBay site code based on the selected site name."""
        return self.site_domain_mapping.get(site_name, {}).get('site', "")  # Site code retrieval

    def get_domain_for_site(self, site_name: str) -> str:
        """Retrieve the domain associated with the given site name."""
        site_info = self.site_domain_mapping.get(site_name, {})
        return site_info.get('domain', "")

    def connect_to_api(self, api_details: dict) -> str:
        """Handle the API connection process."""
        LoggingService.log(f"Attempting to connect to eBay API with details: {api_details}", level="info")

        try:
            message = self.ebay_service.connect(api_details)
            LoggingService.log(f"Connection to eBay API successful: {message}", level="info")
            return message
        except Exception as e:
            error_message = f"Failed to connect to eBay API: {str(e)}"
            LoggingService.log(error_message, level="error")
            raise Exception(error_message)
