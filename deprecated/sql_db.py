import pymysql
from pymysql import Error
from config.database_config import get_db_config

class DatabaseEbay:
    def __init__(self):
        self.db_config = get_db_config()
        try:
            self.conn = pymysql.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            print("Database connection established.")
        except Error as e:
            print(f"Error establishing database connection: {e}")
            raise

    def insert_data(self, data, query):
        try:
            if data.get("item_information"):
                self.cursor.execute("""
                      INSERT IGNORE INTO ItemInformation 
                      (itemId, title, categoryId, categoryName, galleryURL, viewItemURL, productId, listingType, conditionId, 
                      conditionDisplayName, isMultiVariationListing, topRatedListing, query_string)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                  """, (*data["item_information"], query))

            if data.get("location_information"):
                self.cursor.execute("""
                    INSERT IGNORE INTO LocationInformation 
                    (itemId, postalCode, location, country)
                    VALUES (%s, %s, %s, %s)
                """, data["location_information"])

            if data.get("shipping_information"):
                self.cursor.execute("""
                    INSERT IGNORE INTO ShippingInformation 
                    (itemId, shippingCost, shippingType, expeditedShipping, oneDayShippingAvailable, handlingTime)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, data["shipping_information"])

            if data.get("pricing_and_sales"):
                self.cursor.execute("""
                    INSERT IGNORE INTO PricingAndSales 
                    (itemId, currentPrice, convertedCurrentPrice, bestOfferEnabled, buyItNowAvailable, startTime, endTime)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, data["pricing_and_sales"])

            if data.get("additional_attributes"):
                self.cursor.execute("""
                    INSERT IGNORE INTO AdditionalItemAttributes 
                    (itemId, globalId, autoPay, timeLeft, gift, watchCount, returnsAccepted, sellingState)call
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, data["additional_attributes"])

            self.conn.commit()
            print("Data successfully inserted into database.")
        except Exception as e:
            print(f"Error inserting data: {e}")

    def close_connection(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()
        if hasattr(self, 'conn'):
            self.conn.close()
        print("Database connection closed.")

        print("Database connection closed.")