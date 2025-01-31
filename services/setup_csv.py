from PySide6.QtCore import Signal, QObject
import pandas as pd

class CsvSetup(QObject):
    csv_loaded = Signal(list, list)  # Emit columns and rows

    def __init__(self):
        super().__init__()

    def load_csv(self, file_path):
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                df = pd.read_excel(file_path, engine='openpyxl')
            else:
                raise ValueError("Unsupported file format.")

            if df.empty:
                raise ValueError("The file is empty or could not be read.")

            columns = df.columns.tolist()
            rows = df.values.tolist()
            self.csv_loaded.emit(columns, rows)

        except pd.errors.EmptyDataError:
            self.csv_loaded.emit([], [])
            raise RuntimeError("The selected file is empty.")

        except pd.errors.ParserError:
            self.csv_loaded.emit([], [])
            raise RuntimeError("Error parsing the file. Please check its format.")

        except Exception as e:
            self.csv_loaded.emit([], [])
            raise RuntimeError(f"Unexpected error loading file: {e}")
