import sys

# from core import EbayItemFetcher
from PySide6.QtWidgets import QApplication

from controllers.controller_main import MainController
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application
    window = MainController()  # Create the window
    window.show()  # Show the window
    sys.exit(app.exec())  # Start the application event loop
    # EbayScrapper = EbayItemFetcher.EbayScraping()
    # EbayScrapper.check_app_id()
    # EbayScrapper.connect_to_ebay()
    # EbayScrapper.scrap_ebay()



