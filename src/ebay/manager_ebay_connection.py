from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from logger.service_logging import LoggingService


class EbayConnectionManager:
    def __init__(
            self,
            logger: LoggingService,
            api_details: dict
    ):
        # Initialize with API details and logger
        self.api_id = api_details['API_ID']
        self.api_domain = api_details['API_DOMAIN']
        self.api_site_id = api_details['API_SITE_ID']
        self.logger = logger  # Use the passed logger instancce

    def connect_to_ebay(self):
        """Attempt to connect to eBay API and handle any connection errors."""
        self.logger.log(
            f"Attempting to connect to eBay API with domain {self.api_domain} and site ID {self.api_site_id}...",
            level="info")

        try:
            # Create the API connection
            api = Connection(
                appid=self.api_id,
                config_file=None,
                siteid=self.api_site_id
            )

            # Log success
            self.logger.log(f"Successfully connected to eBay API for site {self.api_domain}.", level="info")
            return api

        except ConnectionError as e:
            # Log error details and raise the exception
            error_message = f"Error: Connection failed. Details: {e}"
            self.logger.log(error_message, level="error")
            raise ConnectionError(error_message)