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

            columns = df.columns.tolist()
            rows = df.values.tolist()
            self.csv_loaded.emit(columns, rows)

        except Exception as e:
            self.csv_loaded.emit([], [])  # Emit empty if error
            raise RuntimeError(f"Error loading file: {e}")
