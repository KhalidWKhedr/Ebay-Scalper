from logger.service_logging import LoggingService
from src.controllers.controller_csv import CsvController
from src.controllers.controller_database import DatabaseController
from src.controllers.controller_ebay_api import EbayApiController
from src.models.model_database_connection_details import SchemaConnectionDetails
from src.services.service_csv import CsvService
from src.services.service_database import DatabaseService
from src.services.service_ebay import EbayService
from src.services.service_notification import NotificationService
from src.ui.presenter_csv import CsvPresenter
from src.ui.presenter_database import DatabaseWindowPresenter
from src.ui.presenter_ebay import EbayWindowPresenter
from utils.converter import Converter


class MainPresenter:
    def __init__(
        self,
        db_service: DatabaseService,
        logger: LoggingService,
        converter: Converter,
        notification_service: NotificationService,
        ebay_service: EbayService,
        csv_service: CsvService,
        schema_connection_details: SchemaConnectionDetails,
        csv_presenter: CsvPresenter,
    ):
        self.db_service = db_service
        self.logger = logger
        self.converter = converter
        self.notification_service = notification_service
        self.ebay_service = ebay_service
        self.csv_service = csv_service
        self.schema_connection_details = schema_connection_details
        self.csv_presenter = csv_presenter


        self.csv_controller = CsvController(csv_service, notification_service)
        self.database_controller = DatabaseController(
            db_service, logger, converter, notification_service, schema_connection_details
        )
        self.ebay_controller = EbayApiController(ebay_service, notification_service, logger)

        self.database_window = None
        self.ebay_window = None

    def open_database_window(self) -> None:
        try:
            if not self.database_window or not self.database_window.isVisible():
                self.database_window = DatabaseWindowPresenter(
                    self.database_controller, schema_connection_details=self.schema_connection_details
                )
            self.database_window.show()
        except Exception as e:
            self.logger.error(f"Failed to open database window: {e}")
            self.notification_service.notify(f"Error: {e}")

    def open_ebay_window(self) -> None:
        try:
            if not self.ebay_window or not self.ebay_window.isVisible():
                self.ebay_window = EbayWindowPresenter(self.ebay_controller)
            self.ebay_window.show()
        except Exception as e:
            self.logger.error(f"Failed to open eBay window: {e}")
            self.notification_service.notify(f"Error: {e}")

    def perform_csv_operation(self, file_path: str) -> None:
        try:
            self.csv_controller.load_csv(file_path)
            self.notification_service.notify("CSV file loaded successfully.")
        except Exception as e:
            self.logger.error(f"Failed to perform CSV operation: {e}")
            self.notification_service.notify(f"Error: {e}")