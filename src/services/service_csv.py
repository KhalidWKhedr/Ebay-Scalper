from PySide6.QtCore import Signal, QObject
import pandas as pd
from src.logger.service_logging import LoggingService


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
                raise ValueError("Unsupported file format. Only .csv and .xlsx files are supported.")

            # Check if the file is empty
            if df.empty:
                raise ValueError("The file is empty or could not be read.")

            # Prepare columns and rows for emission
            columns = df.columns.tolist()
            rows = df.values.tolist()
            self.csv_loaded.emit(columns, rows, "")  # Emit data with no error

        except pd.errors.EmptyDataError:
            error_msg = "The selected file is empty or could not be read."
            self.csv_loaded.emit([], [], error_msg)
            self.logger.error(error_msg)

        except pd.errors.ParserError as e:
            error_msg = f"Error parsing the file: {e}. Please check its format."
            self.csv_loaded.emit([], [], error_msg)
            self.logger.error(error_msg)

        except ValueError as e:
            error_msg = f"Value error: {e}"
            self.csv_loaded.emit([], [], error_msg)
            self.logger.error(error_msg)

        except Exception as e:
            error_msg = f"Unexpected error loading file: {e}"
            self.csv_loaded.emit([], [], error_msg)
            self.logger.error(error_msg)