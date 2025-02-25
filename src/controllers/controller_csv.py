from src.logger.service_logging import LoggingService
from src.services.service_csv import CsvService

class CsvController:
    def __init__(
        self,
        logger: LoggingService,
        csv_service: CsvService,
    ):
        """
        Initialize the CsvController with the given services.

        :param logger: An instance of LoggingService for logging messages.
        :param csv_service: An instance of CsvService for handling CSV file operations.
        """
        self.logger = logger
        self.csv_service = csv_service

    def load_csv(self, file_path: str):
        """
        Trigger the loading of a CSV file from the given file path.

        :param file_path: The path of the CSV file to be loaded.
        """
        try:
            print(f"Loading CSV file: {file_path}")  # Debug log
            self.csv_service.load_csv(file_path)
            self.logger.get_logger().info(f"Loading CSV file from: {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to load CSV file from {file_path}: {e}")
            raise  # Optionally re-raise or handle differently based on your use case