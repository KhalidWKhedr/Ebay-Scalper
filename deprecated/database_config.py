import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_config():
    return {
        'user': os.getenv('DB_USER', 'default_user'),
        'password': os.getenv('DB_PASSWORD', 'default_password'),
        'host': os.getenv('DB_HOST', 'localhost'),
        'database': os.getenv('DB_NAME', 'EbayListings')
    }
