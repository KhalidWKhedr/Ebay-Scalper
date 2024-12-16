
from core import EbayItemFetcher
from PySide6.QtWidgets import QDialog

from backend.gui2 import Ui_form_db_connection



class MainWindow(QDialog, Ui_form_db_connection):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Set up the UI on this dialog


if __name__ == '__main__':
    # app = QApplication(sys.argv)  # Create the application
    # window = MainWindow()  # Create the window
    # window.show()  # Show the window
    # sys.exit(app.exec())  # Start the application event loop
    EbayScrapper = EbayItemFetcher.EbayScraping()
    EbayScrapper.check_app_id()
    EbayScrapper.connect_to_ebay()
    EbayScrapper.scrap_ebay()



