from functools import partial

from PySide6.QtWidgets import QPushButton, QListWidgetItem, QFileDialog

from services.service_csv import CsvService
from services.service_notification import NotificationService


class CsvController:
    def __init__(self, main_ui, csv_service: CsvService, notification_service: NotificationService):
        self.ui = main_ui
        self.csv_service = csv_service
        self.notification_service = notification_service

        # Connect the signal to the slot
        self.csv_service.csv_loaded.connect(self.handle_csv_loaded)

        # Connect UI actions to methods
        self.ui.actionImport_CSV.triggered.connect(self.open_file_dialog)

    def open_file_dialog(self):
        """Opens file dialog and loads CSV. Enhances UI experience."""
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Open CSV File", "", "CSV Files (*.csv);;Excel Files (*.xlsx)"
        )
        if file_path:
            self.load_csv(file_path)

    def load_csv(self, file_path):
        """Handles CSV loading and error display, with proper feedback."""
        try:
            # Show loading feedback to user
            pass
            #self.notification_service.show_loading("Loading CSV...")

            # Load the CSV using the service
            self.csv_service.load_csv(file_path)

        except RuntimeError as e:
            # Error handling and UI feedback
            self.notification_service.show_message(self.ui, f"Error: {str(e)}")

        finally:
            # Hide loading indicator once the task is complete
            pass
            #self.notification_service.hide_loading()

    def handle_csv_loaded(self, columns, rows):
        """Handles UI update when CSV is loaded."""
        if not columns:
            self.notification_service.show_message(self.ui, "Failed to load CSV.")
            return

        print("CSV Loaded:", columns, rows)
        self.populate_column_buttons(columns)

    def populate_column_buttons(self, columns):
        """Dynamically adds buttons for CSV columns, creating interactive UI elements."""
        self.ui.listWidget.clear()
        for column in columns:
            button = QPushButton(column)
            button.clicked.connect(partial(self.on_column_button_clicked, column))
            list_item = QListWidgetItem(self.ui.listWidget)
            self.ui.listWidget.addItem(list_item)
            self.ui.listWidget.setItemWidget(list_item, button)

    def on_column_button_clicked(self, column_name):
        """Handles column button click."""
        print(f"Column {column_name} button clicked!")
