import sys

# from core import EbayItemFetcher
from PySide6.QtWidgets import QApplication

from controllers.controller_main import MainController
from database.service_database import DatabaseService
from logger.service_logging import LoggingService
from services.ebay.service_ebay import EbayService
from services.service_notification import NotificationService
from utils.converter import Converter
from services.service_csv import CsvService

logger = LoggingService()
database_service = DatabaseService()
utils_converter = Converter()
service_notification = NotificationService()
service_ebay = EbayService()
service_csv = CsvService()
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application
    window = MainController(
            db_service=database_service,
            logger=logger,
            converter=utils_converter,
            notification_service=service_notification,
            ebay_service=service_ebay,
            csv_service = service_csv)  # Create the window
    window.show()  # Show the window
    sys.exit(app.exec())  # Start the application event loop
    # EbayScrapper = EbayItemFetcher.EbayScraping()
    # EbayScrapper.check_app_id()
    # EbayScrapper.connect_to_ebay()
    # EbayScrapper.scrap_ebay()



