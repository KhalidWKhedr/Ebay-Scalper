from PySide6.QtCore import Signal, QObject
import pandas as pd


class CSV_Setup(QObject):
    csv_loaded = Signal(list, list)  # Signal to emit when CSV is loaded (columns, rows)

    def __init__(self):
        super().__init__()
        self.csv_columns = []
        self.csv_rows = []

    def load_csv(self, file_path):
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                df = pd.read_excel(file_path, engine='openpyxl')
            else:
                raise ValueError("Unsupported file format.")

            self.csv_columns = df.columns.tolist()
            self.csv_rows = df.values.tolist()

            # Emit signal with data
            self.csv_loaded.emit(self.csv_columns, self.csv_rows)

        except Exception as e:
            self.csv_loaded.emit([], [])  # Emit empty if error occurs
            raise RuntimeError(f"Error loading file: {e}")
