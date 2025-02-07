from logger.service_logging import LoggingService
from src.controllers.controller_csv import CsvController
from src.controllers.controller_database import DatabaseController
from src.controllers.controller_ebay_api import EbayApiController
from src.models.model_database_connection_details import SchemaConnectionDetails
from src.services.service_notification import NotificationService
from src.ui.presenter_database import DatabaseWindowPresenter
from src.ui.presenter_ebay import EbayWindowPresenter


class MainPresenter:
    def __init__(
        self,
        logger: LoggingService,
        notification_service: NotificationService,
        csv_controller: CsvController,
        database_controller: DatabaseController,
        ebay_controller: EbayApiController,
    ):
        self.logger = logger
        self.notification_service = notification_service

        # Injected controllers
        self.csv_controller = csv_controller
        self.database_controller = database_controller
        self.ebay_controller = ebay_controller

        # Initialize windows
        self.database_window = None
        self.ebay_window = None

    def open_database_window(self) -> None:
        """Opens the database window."""
        try:
            if not self.database_window or not self.database_window.isVisible():
                # Create SchemaConnectionDetails dynamically when needed
                connection_details = SchemaConnectionDetails(**self.database_controller.get_connection_settings())

                self.database_window = DatabaseWindowPresenter(self.notification_service,
                                                               self.database_controller,
                                                               schema_connection_details=connection_details
                )
            self.database_window.show()
        except Exception as e:
            self._handle_error("Failed to open database window", e)

    def open_ebay_window(self) -> None:
        """Opens the eBay window."""
        try:
            if not self.ebay_window or not self.ebay_window.isVisible():
                self.ebay_window = EbayWindowPresenter(self.notification_service,
                                                       self.ebay_controller)
            self.ebay_window.show()
        except Exception as e:
            self._handle_error("Failed to open eBay window", e)

    def perform_csv_operation(self, file_path: str) -> None:
        """Performs a CSV operation (e.g., loading a CSV file)."""
        try:
            self.csv_controller.load_csv(file_path)
            self.notification_service.notify("CSV file loaded successfully.")
        except Exception as e:
            self._handle_error("Failed to perform CSV operation", e)

    def _handle_error(self, message: str, error: Exception) -> None:
        """Handles errors by logging and notifying the user."""
        self.logger.error(f"{message}: {error}")
        self.notification_service.notify(f"Error: {error}")

