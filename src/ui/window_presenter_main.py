from PySide6.QtWidgets import QMainWindow
from logger.service_logging import LoggingService
from src.controllers.controller_database import DatabaseController
from src.controllers.controller_ebay_api import EbayApiController
from src.models.model_database_connection_details import SchemaConnectionDetails
from src.services.service_csv import CsvService
from src.services.service_database import DatabaseService
from src.services.service_ebay import EbayService
from src.services.service_notification import NotificationService
from src.ui.window_presenter_database import DatabaseWindowPresenter
from src.ui.window_presenter_ebay import EbayWindowPresenter
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
    ):
        self.db_service = db_service
        self.logger = logger
        self.converter = converter
        self.notification_service = notification_service
        self.ebay_service = ebay_service
        self.csv_service = csv_service
        self.schema_connection_details = schema_connection_details

        # Initialize the windows
        self.database_window = None
        self.ebay_window = None

    def open_database_window(self) -> None:
        try:
            if not self.database_window or not self.database_window.isVisible():
                database_controller = DatabaseController(
                    self.db_service,
                    self.logger,
                    self.converter,
                    self.notification_service,
                    self.schema_connection_details,
                )
                self.database_window = DatabaseWindowPresenter(
                    database_controller, schema_connection_details=self.schema_connection_details
                )
            self.database_window.show()
        except Exception as e:
            self.logger.error(f"Failed to open database window: {e}")
            self.notification_service.notify(f"Error: {e}")

    def open_ebay_window(self) -> None:
        try:
            if not self.ebay_window or not self.ebay_window.isVisible():

                ebay_controller = EbayApiController(
                    self.ebay_service,
                    self.notification_service,
                    self.logger,
                )
                self.ebay_window = EbayWindowPresenter(ebay_controller)
            self.ebay_window.show()
        except Exception as e:
            self.logger.error(f"Failed to open eBay window: {e}")
            self.notification_service.notify(f"Error: {e}")