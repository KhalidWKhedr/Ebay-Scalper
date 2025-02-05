from PySide6.QtWidgets import QMainWindow
from gui.gui_form_main import Ui_form_MainWindow
from logger.service_logging import LoggingService
from src.controllers.controller_csv import CsvController
from src.models.model_database_connection_details import SchemaConnectionDetails
from src.services.service_csv import CsvService
from src.services.service_database import DatabaseService
from src.services.service_ebay import EbayService
from src.services.service_notification import NotificationService
from src.ui.presenter_main import MainPresenter
from src.ui.presenter_csv import CsvPresenter
from utils.converter import Converter


class MainController(QMainWindow, Ui_form_MainWindow):
    def __init__(
        self,
        db_service: DatabaseService,
        logger: LoggingService,
        converter: Converter,
        notification_service: NotificationService,
        ebay_service: EbayService,
        csv_service: CsvService,
        schema_connection_details: SchemaConnectionDetails,
    ):
        super().__init__()
        self.setupUi(self)

        # Store injected dependencies
        self.db_service = db_service
        self.logger = logger
        self.converter = converter
        self.notification_service = notification_service
        self.ebay_service = ebay_service
        self.csv_service = csv_service
        self.schema_connection_details = schema_connection_details

        # Initialize controllers and presenters
        self.csv_controller = self._initialize_csv_controller()
        self.csv_presenter = self._initialize_csv_presenter()
        self.presenter = self._initialize_main_presenter()

        # Connect UI buttons to presenter methods
        self._connect_ui_actions()

    def _initialize_csv_controller(self) -> CsvController:
        """Initialize and return the CSV controller."""
        return CsvController(self.csv_service, self.notification_service)

    def _initialize_csv_presenter(self) -> CsvPresenter:
        """Initialize and return the CSV presenter."""
        return CsvPresenter(self, self.csv_controller, self.notification_service)

    def _initialize_main_presenter(self) -> MainPresenter:
        """Initialize and return the main presenter."""
        return MainPresenter(
            self.db_service,
            self.logger,
            self.converter,
            self.notification_service,
            self.ebay_service,
            self.csv_service,
            self.schema_connection_details,
            self.csv_presenter,
        )

    def _connect_ui_actions(self):
        """Connect UI buttons to their respective presenter methods."""
        self.button_DATABASE.clicked.connect(self.presenter.open_database_window)
        self.button_EBAY.clicked.connect(self.presenter.open_ebay_window)