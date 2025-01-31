from logger import LoggingService
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

class EbayConnectionManager:
    def __init__(self, api_details):
        self.api_id = api_details['api_id']
        self.api_domain = api_details['api_domain']
        self.api_site_id = api_details['api_site_id']
        self.logger = LoggingService

    def check_app_id(self):
        if not self.api_id:
            raise ValueError("Missing required environment variable APP_ID.")

    def connect_to_ebay(self):
        try:
            api = Connection(
                appid=self.api_id,
                config_file=None,
                domain=self.api_domain,
                siteid=self.api_site_id
            )
            return api
        except ConnectionError as e:
            self.logger.log(f"Error: Connection failed. Details: {e}", level="error")
            raise
