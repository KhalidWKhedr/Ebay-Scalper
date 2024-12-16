from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QFileDialog, QMessageBox, QPushButton, QListWidgetItem
import pandas as pd

class CSV_Setup(QObject):
    csv_loaded = Signal()  # Signal to emit when CSV is loaded

    def __init__(self):
        super().__init__()
        self.csv_columns = []
        self.csv_rows = []

    def load_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Open File",
            "",
            "Spreadsheet Files (*.output_csv *.xlsx)"
        )
        if file_path:
            try:
                if file_path.endswith('.output_csv'):
                    df = pd.read_csv(file_path)
                    self.csv_columns = df.columns.tolist()
                    self.csv_rows = df.values.tolist()
                elif file_path.endswith('.xlsx'):
                    df = pd.read_excel(file_path, engine='openpyxl')
                    self.csv_columns = df.columns.tolist()
                    self.csv_rows = df.values.tolist()
                else:
                    QMessageBox.warning(None, "Error", "Unsupported file format.")
                    return
                print(self.csv_columns)
                print(self.csv_rows)
                for x in self.csv_rows:
                    print(x)
                self.csv_loaded.emit()  # Emit signal to notify CSV has loaded

            except Exception as e:
                QMessageBox.critical(None, "Error", f"Error loading file: {e}")

    def populate_column_buttons(self, list_widget):
        # Clear any existing items in the list widget
        list_widget.clear()

        # Iterate over CSV columns and create buttons for each
        for column in self.csv_columns:
            button = QPushButton(column)
            button.clicked.connect(lambda _, col=column: self.on_column_button_clicked(col))
            list_item = QListWidgetItem(list_widget)
            list_widget.addItem(list_item)
            list_widget.setItemWidget(list_item, button)

    def on_column_button_clicked(self, column_name):
        # Define what happens when a column button is clicked
        print(f"Column {column_name} button clicked!")
