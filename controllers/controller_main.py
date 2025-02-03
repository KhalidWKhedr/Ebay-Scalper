from PySide6.QtWidgets import QMainWindow
from controllers.controller_database import DatabaseController
from controllers.controller_ebay_api import EbayApiController
from controllers.controller_csv import CsvController
from gui.gui_form_main import Ui_form_MainWindow
from database.service_database import DatabaseService
from services.service_notification import NotificationService
from logger.service_logging import LoggingService
from utils.converter import Converter

class MainController(QMainWindow, Ui_form_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Instantiate CSV Controller (Pass UI reference)
        self.csv_controller = CsvController(self)

        # Initialize your services (can be injected later)
        self.db_service = DatabaseService()
        self.logger = LoggingService()
        self.converter = Converter()
        self.notification_service = NotificationService()

        # Button connections for opening other windows
        self.button_DATABASE.clicked.connect(self.open_database_window)
        self.button_EBAY.clicked.connect(self.open_ebay_window)

        # Controllers for separate windows
        self.database_window = None
        self.ebay_window = None

    def open_database_window(self):
        if not self.database_window:
            # Pass the required dependencies to the DatabaseController
            self.database_window = DatabaseController(
                self.db_service,
                self.logger,
                self.converter,
                self.notification_service
            )
        self.database_window.show()

    def open_ebay_window(self):
        if not self.ebay_window:
            self.ebay_window = EbayApiController()
        self.ebay_window.show()
