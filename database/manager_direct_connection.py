from urllib.parse import quote
import pymongo
from logger import service_logging

class NormalConnectionManager:
    def __init__(self, connection_details):
        self.mongo_host = connection_details['host']
        self.mongo_port = connection_details['port']
        self.mongo_user = connection_details['user']
        self.mongo_password = connection_details['password']
        self.db_name = connection_details['db_name']
        self.auth_source = connection_details['auth_source']
        self.logger = service_logging.LoggingService.get_logger()
        self.client = None

    def connect(self):
        """Handles the connection to MongoDB without SSH tunneling."""
        try:
            escaped_user = quote(self.mongo_user)
            escaped_password = quote(self.mongo_password)
            uri = f"mongodb://{escaped_user}:{escaped_password}@{self.mongo_host}:{self.mongo_port}:{self.mongo_port}/{self.db_name}?authSource={self.auth_source}"


            self.client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
            self.client.admin.command("ping")

            self.logger.info(f"Successfully connected to MongoDB at {self.mongo_host}:{self.mongo_port}, database: {self.db_name}")
            return self.client

        except Exception as e:
            self.logger.error(f"Failed to connect to MongoDB at {self.mongo_host}:{self.mongo_port}, database: {self.db_name}. Error: {repr(e)}")
            self.client = None
            return None

    def close(self):
        """Closes the MongoDB connection."""
        if self.client:
            self.client.close()
            self.logger.info("MongoDB connection closed.")
            self.client = None
