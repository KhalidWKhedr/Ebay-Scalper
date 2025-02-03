import sys

# from core import EbayItemFetcher
from PySide6.QtWidgets import QApplication

from controllers.controller_main import MainController
from database.service_database import DatabaseService
from logger.service_logging import LoggingService
from services.ebay.service_ebay import EbayService
from services.service_notification import NotificationService
from utils.converter import Converter

db_service = DatabaseService()
logger = LoggingService()
converter = Converter()
notification_service = NotificationService()
ebay_service = EbayService()
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application
    window = MainController(
    db_service=db_service,
    logger=logger,
    converter=converter,
    notification_service=notification_service,
    ebay_service=ebay_service)  # Create the window
    window.show()  # Show the window
    sys.exit(app.exec())  # Start the application event loop
    # EbayScrapper = EbayItemFetcher.EbayScraping()
    # EbayScrapper.check_app_id()
    # EbayScrapper.connect_to_ebay()
    # EbayScrapper.scrap_ebay()



