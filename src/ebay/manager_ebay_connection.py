from logger import service_logging
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

class EbayConnectionManager:
    def __init__(self, api_details):
        self.api_id = api_details['API_ID']
        self.api_domain = api_details['API_DOMAIN']
        self.api_site_id = api_details['API_SITE_ID']
        self.logger = service_logging

    def check_app_id(self):
        if not self.api_id:
            raise ValueError("Missing required environment variable APP_ID.")

    def connect_to_ebay(self):
        try:
            self.check_app_id()
            api = Connection(
                appid=self.api_id,
                config_file=None,
                domain=self.api_domain,
                siteid=self.api_site_id
            )
            return api
        except ConnectionError as e:
            self.logger.LoggingService.log(f"Error: Connection failed. Details: {e}", level="error")
            raise
