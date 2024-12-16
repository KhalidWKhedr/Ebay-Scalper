import os
import time
import pandas as pd
from dotenv import load_dotenv
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from core.MongoDBOperations import MongoDBOperations  # Corrected class name
from core.MongoSSHConnector import MongoSSHConnector
from core.EbayJsonExtractor import EbayJsonExtractor
load_dotenv('config/.env')

class EbayScraping:
    def __init__(self):
        self.data_to_search = pd.read_excel("query_csv/Cleaned_Spiele_Spielzeug.xlsx", usecols=[0], skiprows=0)
        self.column_data = self.data_to_search.iloc[:, 0].tolist()
        self.app_id = os.getenv("APP_ID")
        self.check_app_id()

    def check_app_id(self):
        """Ensure the APP_ID environment variable is set."""
        if not self.app_id:
            raise ValueError("Missing required environment variable APP_ID.")

    def connect_to_ebay(self):
        """Establish a connection to the eBay API."""
        try:
            api = Connection(appid=self.app_id, config_file=None, domain='svcs.ebay.com')
            return api
        except ConnectionError as e:
            print(f"Error: Connection failed. Details: {e}")
            raise

    def scrap_ebay(self):
        """Main method for scraping eBay data."""
        api = self.connect_to_ebay()
        mongo_connector = MongoSSHConnector('config/.env')
        mongo_connector.connect()

        mongo_operations = MongoDBOperations(mongo_connector.client)

        for query in self.column_data:
            self.scrape_and_store(api, query, mongo_operations)

        mongo_connector.close_connection()

    def scrape_and_store(self, api, query, mongo_operations):
        """Handle the actual scraping and insertion of eBay data."""
        try:
            response = api.execute('findItemsAdvanced', {'keywords': query}).dict()

            if response.get('ack') == 'Success':
                items = response.get('searchResult', {}).get('item', [])
                if items:
                    self.process_items(items, query, mongo_operations)
                else:
                    print(f"No items found for '{query}'.")
            else:
                print(f"API call failed for '{query}'. Response: {response}")
        except Exception as e:
            print(f"Error scraping for '{query}': {e}")

    def process_items(self, items, query, mongo_operations):
        """Process individual items and insert them into MongoDB."""
        for item in items:
            print(item)
            extractor = EbayJsonExtractor(item)
            extracted_data = extractor.extract_data()
            extracted_data['query_string'] = query
            mongo_operations.insert_data(extracted_data, query)

