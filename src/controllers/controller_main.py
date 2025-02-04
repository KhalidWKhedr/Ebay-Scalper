from PySide6.QtWidgets import QMainWindow

from gui.gui_form_main import Ui_form_MainWindow
from logger.service_logging import LoggingService
from src.models.model_database_connection_details import SchemaConnectionDetails
from src.services.service_csv import CsvService
from src.services.service_database import DatabaseService
from src.services.service_ebay import EbayService
from src.services.service_notification import NotificationService
from src.ui.window_presenter_main import MainPresenter
from utils.converter import Converter

class MainController(QMainWindow, Ui_form_MainWindow):
    def __init__(self, db_service: DatabaseService, logger: LoggingService,
                 converter: Converter, notification_service: NotificationService,
                 ebay_service: EbayService, csv_service: CsvService, schema_connection_details: SchemaConnectionDetails):
        super().__init__()
        self.setupUi(self)

        # Injected dependencies
        self.db_service = db_service
        self.logger = logger
        self.converter = converter
        self.notification_service = notification_service
        self.ebay_service = ebay_service
        self.csv_service = csv_service
        self.schema_connection_details = schema_connection_details

        # Instantiate the presenter
        self.presenter = MainPresenter(self.db_service, self.logger, self.converter,
                                       self.notification_service, self.ebay_service,
                                       self.csv_service, self.schema_connection_details)

        # Connect the UI buttons to the presenter's methods
        self.button_DATABASE.clicked.connect(self.presenter.open_database_window)
        self.button_EBAY.clicked.connect(self.presenter.open_ebay_window)
