from PySide6.QtWidgets import QMainWindow
from gui.gui_form_main import Ui_form_MainWindow
from logger.service_logging import LoggingService
from src.controllers.controller_csv import CsvController
from src.controllers.controller_database import DatabaseController
from src.controllers.controller_ebay_api import EbayApiController
from src.config.site_domain_mapping_ebay import SITE_DOMAIN_MAPPING
from src.services.service_csv import CsvService
from src.services.service_database import DatabaseService
from src.services.service_ebay import EbayService
from src.services.service_notification import NotificationService
from src.ui.presenter_main import MainPresenter
from src.ui.presenter_csv import CsvPresenter
from utils.converter import Converter
from src.models.model_site_domain_ebay import SiteDomainModel


class MainController(QMainWindow, Ui_form_MainWindow):
    def __init__(
        self,
        db_service: DatabaseService,
        logger: LoggingService,
        converter: Converter,
        notification_service: NotificationService,
        ebay_service: EbayService,
        csv_service: CsvService,
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

        # Initialize Models
        self.site_domain_model = SiteDomainModel(SITE_DOMAIN_MAPPING)

        # Initialize Controllers & Presenters
        self._initialize_controllers()
        self._initialize_presenters()

        # Connect UI actions
        self._connect_ui_actions()

    def _initialize_controllers(self):
        """Initialize and store controllers."""
        self.logger.log("Initializing controllers...", level="info")

        self.csv_controller = CsvController(self.csv_service, self.notification_service)
        self.database_controller = DatabaseController(
            self.db_service, self.logger, self.converter, self.notification_service
        )
        self.ebay_controller = EbayApiController(
            self.ebay_service, self.notification_service, self.logger, self.site_domain_model
        )

    def _initialize_presenters(self):
        """Initialize and store presenters."""
        self.logger.log("Initializing presenters...", level="info")

        self.csv_presenter = CsvPresenter(self, self.csv_controller, self.notification_service)

        self.presenter = MainPresenter(
            db_service=self.db_service,
            logger=self.logger,
            converter=self.converter,
            notification_service=self.notification_service,
            ebay_service=self.ebay_service,
            csv_service=self.csv_service,
            csv_presenter=self.csv_presenter,
            csv_controller=self.csv_controller,
            database_controller=self.database_controller,
            ebay_controller=self.ebay_controller,
        )

    def _connect_ui_actions(self):
        """Connect UI buttons to presenter methods."""
        self.logger.log("Connecting UI actions...", level="info")

        # Connect the buttons to corresponding presenter methods
        self.button_DATABASE.clicked.connect(self.presenter.open_database_window)
        self.button_EBAY.clicked.connect(self.presenter.open_ebay_window)

