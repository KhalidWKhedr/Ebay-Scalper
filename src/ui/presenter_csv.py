from functools import partial

from PySide6.QtWidgets import QFileDialog, QPushButton, QListWidgetItem


class CsvPresenter:
    def __init__(self, main_ui, csv_controller, notification_service):
        """ Initializes the CsvPresenter. """
        self.ui = main_ui
        self.csv_controller = csv_controller
        self.notification_service = notification_service
        self._connect_ui_actions()
        self._connect_csv_service_signals()

    @staticmethod
    def on_column_button_clicked(column_name):
        """ Handles the click event for a column button. """
        print(f"Column {column_name} button clicked!")

    def _connect_ui_actions(self):
        """Connects UI actions to their respective methods."""
        self.ui.actionImport_CSV.triggered.connect(self.open_file_dialog)

    def _connect_csv_service_signals(self):
        """Connects CSV service signals to their respective handlers."""
        self.csv_controller.csv_service.csv_loaded.connect(self.handle_csv_loaded)

    def open_file_dialog(self):
        """Opens a file dialog to select and load a CSV file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self.ui,
            "Open CSV File",
            "",
            "CSV Files (*.csv);;Excel Files (*.xlsx)"
        )
        if file_path:
            self.csv_controller.load_csv(file_path)

    def handle_csv_loaded(self, columns, rows):
        """ Handles the UI update after a CSV file is loaded. """
        if not columns:
            self.notification_service.show_message(self.ui, "Failed to load CSV.")
            return

        print("CSV Loaded:", columns, rows)
        self.populate_column_buttons(columns)

    def populate_column_buttons(self, columns):
        """ Dynamically adds buttons for each column in the CSV file. """
        self.ui.listWidget.clear()
        for column in columns:
            button = self._create_column_button(column)
            self._add_button_to_list_widget(button, column)

    def _create_column_button(self, column_name):
        """ Creates a QPushButton for a CSV column. """
        button = QPushButton(column_name)
        button.clicked.connect(partial(self.on_column_button_clicked, column_name))
        return button

    def _add_button_to_list_widget(self, button, column_name):
        """ Adds a button to the list widget. """
        list_item = QListWidgetItem(self.ui.listWidget)
        self.ui.listWidget.addItem(list_item)
        self.ui.listWidget.setItemWidget(list_item, button)
        print(f"Added button for column: {column_name}")
