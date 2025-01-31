from PySide6.QtWidgets import QMainWindow
from controllers.database_controller import DatabaseController
from controllers.ebay_api_controller import EbayApiController
from controllers.csv_controller import CsvController
from gui.gui_form_main import Ui_form_MainWindow

class MainController(QMainWindow, Ui_form_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Instantiate CSV Controller (Pass UI reference)
        self.csv_controller = CsvController(self)

        # Button connections for opening other windows
        self.button_DATABASE.clicked.connect(self.open_database_window)
        self.button_EBAY.clicked.connect(self.open_ebay_window)

        # Controllers for separate windows
        self.database_window = None
        self.ebay_window = None

    def open_database_window(self):
        if not self.database_window:
            self.database_window = DatabaseController()
        self.database_window.show()


    def open_ebay_window(self):
        if not self.ebay_window:
            self.ebay_window = EbayApiController()
        self.ebay_window.show()