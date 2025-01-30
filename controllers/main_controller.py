from PySide6.QtWidgets import QMainWindow
from controllers.database_controller import DatabaseController
from controllers.csv_controller import CsvController
from ui.gui_form_main import Ui_form_MainWindow

class MainController(QMainWindow, Ui_form_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Instantiate CSV Controller (Pass UI reference)
        self.csv_controller = CsvController(self)

        # Button connections for opening other windows
        self.button_DATABASE.clicked.connect(self.open_database_window)

        # Controllers for separate windows
        self.database_window = None

    def open_database_window(self):
        if not self.database_window:
            self.database_window = DatabaseController()
        self.database_window.show()
