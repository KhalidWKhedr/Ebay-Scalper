from PySide6.QtWidgets import QFileDialog, QMessageBox, QPushButton, QListWidgetItem

from services.setup_csv import CsvSetup

class CsvController:
    def __init__(self, main_ui):
        self.ui = main_ui
        self.csv_setup = CsvSetup()
        self.csv_setup.csv_loaded.connect(self.on_csv_loaded)
        self.ui.actionImport_CSV.triggered.connect(self.open_file_dialog)

    def open_file_dialog(self):
        """Opens file dialog and loads CSV."""
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Open CSV File", "", "CSV Files (*.csv);;Excel Files (*.xlsx)"
        )
        if file_path:
            self.load_csv(file_path)

    def load_csv(self, file_path):
        """Handles CSV loading and error display."""
        try:
            self.csv_setup.load_csv(file_path)
        except RuntimeError as e:
            QMessageBox.critical(None, "Error", str(e))

    def on_csv_loaded(self, columns, rows):
        """Handles UI update when CSV is loaded."""
        if not columns:
            QMessageBox.warning(None, "Error", "Failed to load CSV.")
            return

        print("CSV Loaded:", columns, rows)
        self.populate_column_buttons(columns)

    def populate_column_buttons(self, columns):
        """Dynamically adds buttons for CSV columns."""
        self.ui.listWidget.clear()
        for column in columns:
            button = QPushButton(column)
            button.clicked.connect(lambda checked=False, col=column: self.on_column_button_clicked(col))  # Fix here
            list_item = QListWidgetItem(self.ui.listWidget)
            self.ui.listWidget.addItem(list_item)
            self.ui.listWidget.setItemWidget(list_item, button)

    def on_column_button_clicked(self, column_name):
        """Handles column button click."""
        print(f"Column {column_name} button clicked!")
