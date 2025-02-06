from logging import Logger

from PySide6.QtCore import QObject, Signal

from logger.service_logging import LoggingService
from src.services.service_csv import CsvService
from src.services.service_notification import NotificationService

class CsvController(QObject):
    """
    Controller class for managing CSV file loading.
    Emits a signal when the CSV is successfully loaded or an error occurs.
    """
    csv_loaded = Signal(list, list)

    def __init__(
        self,
        logger: LoggingService,
        csv_service: CsvService,
        notification_service: NotificationService
    ):
        """
        Initialize the CsvController with the given services.

        :param csv_service: An instance of CsvService for handling CSV file operations.
        :param notification_service: An instance of NotificationService for displaying notifications.
        """
        super().__init__()
        self.logger = logger
        self.csv_service = csv_service
        self.notification_service = notification_service

        # Connect the csv_loaded signal from the service to the controller's signal.
        self.csv_service.csv_loaded.connect(self._on_csv_loaded)

    def load_csv(self, file_path: str):
        """
        Trigger the loading of a CSV file from the given file path.

        :param file_path: The path of the CSV file to be loaded.
        """
        try:
            # Request the CSV service to load the CSV file.
            self.csv_service.load_csv(file_path)
        except RuntimeError as e:
            # Notify the user if an error occurs during CSV loading.
            self.logger.log(f"Error: {str(e)}")

    def _on_csv_loaded(self, csv_data: list, headers: list):
        """
        Handle the successful loading of a CSV file.

        :param csv_data: The list of data loaded from the CSV.
        :param headers: The headers parsed from the CSV.
        """
        # Emit the csv_loaded signal to notify other parts of the application.
        self.csv_loaded.emit(csv_data, headers)
