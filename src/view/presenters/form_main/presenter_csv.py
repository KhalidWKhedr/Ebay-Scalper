from functools import partial
from PySide6.QtWidgets import QFileDialog, QPushButton, QListWidgetItem


class CsvPresenter:
    def __init__(
        self,
        csv_controller,
        notification_service
    ):
        """ Initializes the CsvPresenter. """
        self.main_window = None  # Initialize as None
        self.csv_controller = csv_controller
        self.notification_service = notification_service
        self._connect_csv_service_signals()

    def set_main_window(self, main_window):
        """Sets the main window for the presenter."""
        self.main_window = main_window
        self._connect_ui_actions()  # Connect UI actions after main_window is set

    @staticmethod
    def on_column_button_clicked(column_name):
        """ Handles the click event for a column button. """
        print(f"Column {column_name} button clicked!")

    def _connect_ui_actions(self):
        """Connects UI actions to their respective methods."""
        if hasattr(self.main_window.main_ui, 'actionImport_CSV'):
            self.main_window.main_ui.actionImport_CSV.triggered.connect(self.open_file_dialog)
        else:
            print("Warning: 'actionImport_CSV' is missing in the UI.")

    def _connect_csv_service_signals(self):
        """Connects CSV service signals to their respective handlers."""
        self.csv_controller.csv_service.csv_loaded.connect(self.handle_csv_loaded)

    def open_file_dialog(self):
        """Opens a file dialog to select and load a CSV file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self.main_window,  # Use the QMainWindow instance as the parent
            "Open CSV File",
            "",
            "CSV Files (*.csv);;Excel Files (*.xlsx)"
        )
        if file_path:
            try:
                self.csv_controller.load_csv(file_path)
            except Exception as e:
                self.notification_service.show_message(self.main_window, f"Error loading file: {e}")

    def handle_csv_loaded(self, columns, rows):
        """Handles the UI update after a CSV file is loaded."""
        if not columns:
            self.notification_service.show_message(self.main_window, "Failed to load CSV.")
            return

        print("CSV Loaded:", columns, rows)
        self.populate_column_buttons(columns)

    def populate_column_buttons(self, columns):
        """Dynamically adds buttons for each column in the CSV file."""
        self.main_window.main_ui.listWidget.clear()  # Access listWidget from the main window's UI
        for column in columns:
            button = self._create_column_button(column)
            self._add_button_to_list_widget(button, column)

    def _create_column_button(self, column_name):
        """Creates a QPushButton for a CSV column."""
        button = QPushButton(column_name)
        button.clicked.connect(partial(self.on_column_button_clicked, column_name))
        return button

    def _add_button_to_list_widget(self, button, column_name):
        """Adds a button to the list widget."""
        list_item = QListWidgetItem(self.main_window.main_ui.listWidget)
        self.main_window.main_ui.listWidget.addItem(list_item)
        self.main_window.main_ui.listWidget.setItemWidget(list_item, button)
        print(f"Added button for column: {column_name}")