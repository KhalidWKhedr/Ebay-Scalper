from logger.service_logging import LoggingService
from src.models.model_database_connection_details import SchemaConnectionDetails
from src.services.service_notification import NotificationService
from src.view.presenters.form_database.presenter_database import DatabaseWindowPresenter
from src.view.presenters.form_ebay.presenter_ebay import EbayWindowPresenter
from src.controllers.controller_database import DatabaseController
from src.controllers.controller_ebay_api import EbayApiController
from src.controllers.controller_csv import CsvController


class MainController:
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
                self.database_window = DatabaseWindowPresenter(self.notification_service,
                                                               self.database_controller)
            self.database_window.show()
        except Exception as e:
            self._handle_error("Failed to open database window", e)
            return  # Return early after notifying the user of the error

    def open_ebay_window(self) -> None:
        """Opens the eBay window."""
        try:
            if not self.ebay_window or not self.ebay_window.isVisible():
                self.ebay_window = EbayWindowPresenter(self.notification_service, self.ebay_controller)
            self.ebay_window.show()
        except Exception as e:
            self._handle_error("Failed to open eBay window", e)
            return  # Return early after notifying the user of the error

    def perform_csv_operation(self, file_path: str) -> None:
        """Performs a CSV operation (e.g., loading a CSV file)."""
        try:
            self.csv_controller.load_csv(file_path)
            self.notification_service.notify("CSV file loaded successfully.")
        except Exception as e:
            self._handle_error("Failed to perform CSV operation", e)
            return  # Return early after notifying the user of the error

    def _handle_error(self, message: str, error: Exception) -> None:
        """Handles errors by logging and notifying the user."""
        self.logger.error(f"{message}: {error}")
        self.notification_service.notify(f"Error: {error}")
