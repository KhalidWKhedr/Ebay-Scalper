from logger.service_logging import LoggingService
from src.services.service_ebay import EbayService
from src.services.service_notification import NotificationService
from src.models.model_site_domain_ebay import SiteDomainModel


class EbayApiController:
    def __init__(
        self,
        ebay_service: EbayService,
        notification_service: NotificationService,
        logger: LoggingService,
        site_domain_model: SiteDomainModel,
    ):
        """
        Initialize the EbayApiController with necessary services.

        :param ebay_service: Service responsible for handling eBay API interactions.
        :param notification_service: Service responsible for showing notifications.
        :param logger: Logger for recording events and errors.
        :param site_domain_model: Model for handling site and domain data related to eBay.
        """
        self.logger = logger
        self.ebay_service = ebay_service
        self.site_domain_model = site_domain_model
        self.notification_service = notification_service

    def get_site_code(self, site_name: str) -> str:
        """
        Retrieve the eBay site code based on the selected site name.

        :param site_name: The name of the eBay site.
        :return: The site code corresponding to the site name.
        """
        site_code = self.site_domain_model.get_site_id_for_site_name(site_name) or ""
        self.logger.log(f"Retrieved site code for {site_name}: {site_code}", level="debug")
        return site_code

    def get_domain_for_site(self, site_name: str) -> str:
        """
        Retrieve the domain associated with the given site name.

        :param site_name: The name of the eBay site.
        :return: The domain corresponding to the site name.
        """
        domain = self.site_domain_model.get_domain_for_site(site_name) or ""
        self.logger.log(f"Retrieved domain for {site_name}: {domain}", level="debug")
        return domain

    def save_connection_settings(self, api_details: dict) -> str:
        """
        Save the eBay API connection settings.

        :param api_details: The connection settings for the eBay API.
        :return: A message indicating success or failure.
        """
        try:
            self.logger.log("Saving eBay API connection settings...", level="info")
            self.ebay_service.save_ebay_connection_settings(api_details)
            success_message = "Connection settings saved successfully."
            self.logger.log(success_message, level="info")
            return success_message
        except Exception as e:
            error_message = f"Failed to save connection settings: {str(e)}"
            self.logger.log(error_message, level="error")
            return error_message

    def connect_to_api(self, api_details: dict) -> str:
        """
        Handle the eBay API connection process.

        :param api_details: The API connection details.
        :return: A message indicating the connection status.
        """
        try:
            self.logger.log("Attempting to connect to eBay API...", level="info")
            message = self.ebay_service.connect(api_details)
            self.logger.log(f"Successfully connected to eBay API: {message}", level="info")
            return message
        except Exception as e:
            error_message = f"Failed to connect to eBay API: {str(e)}"
            self.logger.log(error_message, level="error")
            raise Exception(error_message)
