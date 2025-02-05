from functools import partial
from PySide6.QtCore import QObject, Signal
from src.services.service_csv import CsvService
from src.services.service_notification import NotificationService


class CsvController(QObject):
    csv_loaded = Signal(list, list)

    def __init__(
        self,
        csv_service: CsvService,
        notification_service: NotificationService
    ):
        super().__init__()
        self.csv_service = csv_service
        self.notification_service = notification_service

        self.csv_service.csv_loaded.connect(self.csv_loaded)

    def load_csv(self, file_path: str):
        """Loads a CSV file and emits a signal when done."""
        try:

            self.csv_service.load_csv(file_path)
        except RuntimeError as e:
            self.notification_service.show_message(f"Error: {str(e)}")