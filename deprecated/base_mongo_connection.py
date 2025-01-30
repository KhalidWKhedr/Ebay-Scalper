import pymongo

class BaseMongoConnection:
    def __init__(self, mongo_host, mongo_port, mongo_user, mongo_password, mongo_db, auth_db):
        # MongoDB Credentials
        self.mongo_host = mongo_host
        self.mongo_port = mongo_port
        self.mongo_user = mongo_user
        self.mongo_password = mongo_password
        self.mongo_db = mongo_db
        self.auth_db = auth_db

        # MongoDB URI
        self.mongo_uri = f"mongodb://{self.mongo_user}:{self.mongo_password}@{self.mongo_host}:{self.mongo_port}/{self.mongo_db}?authSource={self.auth_db}&authMechanism=SCRAM-SHA-1"
        self.client = None

    def connect(self):
        """Connect to MongoDB (abstracted)."""
        try:
            self.client = pymongo.MongoClient(self.mongo_uri, serverSelectionTimeoutMS=2000)
            # Test the connection by listing databases
            print("Connected to MongoDB.")
            print("Databases:", self.client.list_database_names())
            return True  # Indicate success
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            return False  # Indicate failure

    def close_connection(self):
        """Close MongoDB connection."""
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")

