from PySide6.QtWidgets import QMainWindow

from gui.gui_form_main import Ui_form_MainWindow

from controllers.controller_csv import CsvController
from controllers.controller_database import DatabaseController
from controllers.controller_ebay_api import EbayApiController
from database.service_database import DatabaseService
from logger.service_logging import LoggingService
from services.ebay.service_ebay import EbayService
from services.service_notification import NotificationService
from services.service_csv import CsvService
from utils.converter import Converter


class MainController(QMainWindow, Ui_form_MainWindow):
    def __init__(self, db_service: DatabaseService, logger: LoggingService,
                 converter: Converter, notification_service: NotificationService,
                 ebay_service: EbayService, csv_service: CsvService):
        super().__init__()
        self.setupUi(self)

        # Injected dependencies
        self.db_service = db_service
        self.logger = logger
        self.converter = converter
        self.notification_service = notification_service
        self.ebay_service = ebay_service
        self.csv_service = csv_service

        # Instantiate CSV Controller (Pass UI reference and required services)
        self.csv_controller = CsvController(self, self.csv_service, self.notification_service)

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
            self.ebay_window = EbayApiController(
                self.ebay_service,
                self.notification_service
            )
        self.ebay_window.show()
