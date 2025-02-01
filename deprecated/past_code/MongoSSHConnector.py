import os
import pymongo
from sshtunnel import SSHTunnelForwarder
from urllib.parse import quote_plus
from dotenv import load_dotenv

class MongoSSHConnector:
    def __init__(self, env_file_path):
        # Load environment variables from .env file
        load_dotenv(env_file_path)

        # Get SSH and MongoDB credentials from environment variables
        self.SSH_HOST = os.getenv("SSH_HOST")
        self.SSH_PORT = int(os.getenv("SSH_PORT", 22))  # Default to 22 if not provided
        self.SSH_USER = os.getenv("SSH_USER")
        self.SSH_PASSWORD = os.getenv("SSH_PASSWORD")

        # MongoDB credentials
        self.MONGO_USER = os.getenv("MONGO_USER")
        self.MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
        self.MONGO_HOST = os.getenv("MONGO_HOST", "localhost")  # MongoDB host in SSH tunnel
        self.MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))  # Default MongoDB port
        self.MONGO_DB = "EbayListings"  # Default to 'EbayListings' but can be changed dynamically
        self.AUTH_DB = os.getenv("AUTH_DB", "admin")

        # URL-encode MongoDB credentials to handle special characters
        self.MONGO_USER = quote_plus(self.MONGO_USER)
        self.MONGO_PASSWORD = quote_plus(self.MONGO_PASSWORD)

        # MongoDB URI (connection string)
        self.mongo_uri = f"mongodb://{self.MONGO_USER}:{self.MONGO_PASSWORD}@localhost:27018/{self.MONGO_DB}?authSource={self.AUTH_DB}&authMechanism=SCRAM-SHA-1"
        print(self.mongo_uri)
        self.client = None
        self.tunnel = None

    def create_tunnel(self):
        """Creates the SSH tunnel."""
        try:
            self.tunnel = SSHTunnelForwarder(
                (self.SSH_HOST, self.SSH_PORT),
                ssh_username=self.SSH_USER,
                ssh_password=self.SSH_PASSWORD,
                remote_bind_address=(self.MONGO_HOST, self.MONGO_PORT),
                local_bind_address=("localhost", 27018)  # Local port for the SSH tunnel
            )
            print(self.SSH_HOST, self.SSH_PORT, self.SSH_USER, self.SSH_PASSWORD, self.MONGO_HOST, self.MONGO_PORT)
            self.tunnel.start()
            print("SSH tunnel established.")
        except Exception as e:
            print(f"Error establishing SSH tunnel: {e}")

    def connect(self):
        """Connect to MongoDB via the SSH tunnel."""
        self.create_tunnel()

        try:
            # Connect to MongoDB via the SSH tunnel
            self.client = pymongo.MongoClient(self.mongo_uri, serverSelectionTimeoutMS=2000)

            # Test connection by listing databases
            print(self.mongo_uri)
            print("Connected to MongoDB.")
            print("Databases:", self.client.list_database_names())
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

    def close_connection(self):
        """Close the MongoDB connection and SSH tunnel."""
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")

        if self.tunnel:
            self.tunnel.stop()
            print("SSH tunnel closed.")