from PySide6.QtCore import Signal, QObject
import pandas as pd
from logger.service_logging import LoggingService


class CsvService(QObject):
    csv_loaded = Signal(list, list, str)  # Emit columns, rows, and error message (if any)

    def __init__(
        self,
        logger: LoggingService
    ):
        """
        Initializes CsvService with a logger.

        Args:
            logger (LoggingService): An instance of LoggingService to log messages.
        """
        super().__init__()
        self.logger = logger

    def load_csv(self, file_path: str):
        """
        Load a CSV or Excel file and emit the columns and rows. If any error occurs,
        an error message is emitted.

        Args:
            file_path (str): Path to the file to load.
        """
        try:
            # Determine file type and load the file accordingly
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                df = pd.read_excel(file_path, engine='openpyxl')
            else:
                raise ValueError("Unsupported file format.")

            # Check if the file is empty
            if df.empty:
                raise ValueError("The file is empty or could not be read.")

            # Prepare columns and rows for emission
            columns = df.columns.tolist()
            rows = df.values.tolist()
            self.csv_loaded.emit(columns, rows, "")

        except pd.errors.EmptyDataError:
            # Handle case where the file is empty
            self.csv_loaded.emit([], [], "The selected file is empty or could not be read.")
            self.logger.error("The selected file is empty or could not be read.")

        except pd.errors.ParserError as e:
            # Handle error parsing the file
            self.csv_loaded.emit([], [], f"Error parsing the file: {e}. Please check its format.")
            self.logger.error(f"Error parsing the file: {e}")

        except ValueError as e:
            # Handle other value errors
            self.csv_loaded.emit([], [], f"Value error: {e}")
            self.logger.error(f"Value error: {e}")

        except Exception as e:
            # Handle unexpected errors
            self.csv_loaded.emit([], [], f"Unexpected error loading file: {e}")
            self.logger.error(f"Unexpected error loading file: {e}")
