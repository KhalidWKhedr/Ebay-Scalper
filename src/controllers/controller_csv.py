from PySide6.QtCore import QObject, Signal

from logger.service_logging import LoggingService
from src.services.service_csv import CsvService
from src.services.service_notification import NotificationService

class CsvController:
    def __init__(
        self,
        logger: LoggingService,
        csv_service: CsvService,
        notification_service: NotificationService
    ):
        """
        Initialize the CsvController with the given services.

        :param logger: An instance of LoggingService for logging messages.
        :param csv_service: An instance of CsvService for handling CSV file operations.
        :param notification_service: An instance of NotificationService for displaying notifications.
        """
        self.logger = logger
        self.csv_service = csv_service
        self.notification_service = notification_service

    def load_csv(self, file_path: str):
        """
        Trigger the loading of a CSV file from the given file path.

        :param file_path: The path of the CSV file to be loaded.
        """
        self.csv_service.load_csv(file_path)
