from PySide6.QtWidgets import QMainWindow
from gui.gui_form_main import Ui_form_MainWindow
from src.controllers.controller_csv import CsvController

from src.controllers.controller_main import MainController
from src.services.service_notification import NotificationService
from src.ui.presenter_csv import CsvPresenter


class MainPresenter(QMainWindow, Ui_form_MainWindow, MainController):
    def __init__(
        self,
        main_controller: MainController,
        csv_controller: CsvController,
        notification_service: NotificationService,

    ):
        super().__init__()
        self.setupUi(self)

        self.notification_service = notification_service
        self.main_controller = main_controller
        self.csv_controller = csv_controller
        self.csv_presenter = CsvPresenter(self, self.csv_controller, self.notification_service)  # Initialize CsvPresenter

        self._connect_ui_actions()

    def _connect_ui_actions(self):
        """Connect UI buttons to presenter methods."""
        self.button_DATABASE.clicked.connect(self.main_controller.open_database_window)
        self.button_EBAY.clicked.connect(self.main_controller.open_ebay_window)


