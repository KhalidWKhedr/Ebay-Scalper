from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from src.logger.service_logging import LoggingService


class ConnectorEbay:
    def __init__(
        self,
        logger: LoggingService,
    ):
        # Initialize only with the logger
        self.logger = logger  # Use the passed logger instance

    def connect_to_ebay(self, api_details: dict):
        print(api_details)
        """
        Attempt to connect to eBay API using the provided API details and handle any connection errors.

        Args:
            api_details (dict): A dictionary containing API_ID, API_DOMAIN, and API_SITE_ID.
        """
        # Extract API details
        api_id = api_details['API_ID']
        api_domain = api_details['API_DOMAIN']
        api_site_id = api_details['API_SITE_ID']

        self.logger.log(
            f"Attempting to connect to eBay API with domain {api_domain} and site ID {api_site_id}...",
            level="info")

        try:
            # Create the API connection
            api = Connection(
                appid=api_id,
                config_file=None,
                siteid=api_site_id
            )

            # Log success
            self.logger.log(f"Successfully connected to eBay API for site {api_domain}.", level="info")
            return api

        except ConnectionError as e:
            # Log error details and raise the exception
            error_message = f"Error: Connection failed. Details: {e}"
            self.logger.log(error_message, level="error")
            raise ConnectionError(error_message)