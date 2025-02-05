from logger import service_logging
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

class EbayConnectionManager:
    def __init__(self, api_details):
        self.api_id = api_details['API_ID']
        self.api_domain = api_details['API_DOMAIN']
        self.api_site_id = api_details['API_SITE_ID']
        self.logger = service_logging

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
            self.logger.LoggingService.log(f"Error: Connection failed. Details: {e}", level="error")
            raise
