class MongoDBOperations:
    def __init__(self, mongo_client):
        self.client = mongo_client

    def insert_data(self, data, query_string, db_name="EbayListings", collection_name="Listings"):
        """Insert data into a specified MongoDB database and collection."""
        db = self.client[db_name]
        collection = db[collection_name]

        # Attach query string to the data
        data['query_string'] = query_string

        try:
            collection.insert_one(data)
            print(f"Data for query '{query_string}' inserted successfully.")
        except Exception as e:
            print(f"Error inserting data for query '{query_string}': {e}")

    def fetch_data(self, db_name="EbayListings", collection_name="listings", query={}):
        """Fetch data from MongoDB collection."""
        db = self.client[db_name]
        collection = db[collection_name]
        return collection.find(query)