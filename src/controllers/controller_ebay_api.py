from logger.service_logging import LoggingService
from src.services.service_ebay import EbayService
from src.models.model_site_domain_ebay import SiteDomainModel


class EbayApiController:
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

    def get_site_code(self, site_name: str) -> str:
        """
        Retrieve the eBay site code based on the selected site name.

        :param site_name: The name of the eBay site.
        :return: The site code corresponding to the site name.
        """
        site_code = self.site_domain_model.get_site_id_for_site_name(site_name) or ""
        self.logger.get_logger().debug(f"Retrieved site code for {site_name}: {site_code}")
        return site_code

    def get_domain_for_site(self, site_name: str) -> str:
        """
        Retrieve the domain associated with the given site name.

        :param site_name: The name of the eBay site.
        :return: The domain corresponding to the site name.
        """
        domain = self.site_domain_model.get_domain_for_site(site_name) or ""
        self.logger.get_logger().debug(f"Retrieved domain for {site_name}: {domain}")
        return domain

    def save_connection_settings(self, api_details: dict) -> bool:
        """
        Save the eBay API connection settings.

        :param api_details: The connection settings for the eBay API.
        :return: A boolean indicating whether the operation was successful.
        """
        try:
            self.logger.get_logger().info("Saving eBay API connection settings...")
            self.ebay_service.save_ebay_connection_settings(api_details)
            self.logger.get_logger().info("Connection settings saved successfully.")
            return True
        except Exception as e:
            self.logger.error(f"Failed to save connection settings: {str(e)}")
            return False

    def connect_to_api(self, api_details: dict) -> bool:
        """
        Handle the eBay API connection process.

        :param api_details: The API connection details.
        :return: A boolean indicating whether the connection was successful.
        """
        try:
            self.logger.get_logger().info("Attempting to connect to eBay API...")
            message = self.ebay_service.connect(api_details)
            self.logger.get_logger().info(f"Successfully connected to eBay API: {message}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to connect to eBay API: {str(e)}")
            return False
