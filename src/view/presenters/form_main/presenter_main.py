from PySide6.QtWidgets import QMainWindow
from src.view.gui.gui_form_main import Ui_form_MainWindow
from src.controllers.controller_csv import CsvController
from src.controllers.controller_main import MainController
from src.services.service_notification import NotificationService
from src.view.presenters.form_main.presenter_csv import CsvPresenter


class MainPresenter(QMainWindow):
    def __init__(
        self,
        main_ui: Ui_form_MainWindow,  # Pass the UI form as a dependency
        main_controller: MainController,
        csv_controller: CsvController,
        notification_service: NotificationService,
        csv_presenter: CsvPresenter,  # Pass CsvPresenter as a dependency
    ):
        super().__init__()
        self.main_ui = main_ui
        self.main_ui.setupUi(self)  # Initialize the UI for the QMainWindow

        self.notification_service = notification_service
        self.main_controller = main_controller
        self.csv_controller = csv_controller
        self.csv_presenter = csv_presenter

        # Pass self (QMainWindow) to CsvPresenter
        self.csv_presenter.set_main_window(self)

        self._connect_ui_actions()

    def _connect_ui_actions(self):
        """Connect UI buttons to presenter methods."""
        self.main_ui.button_DATABASE.clicked.connect(self.main_controller.open_database_window)
        self.main_ui.button_EBAY.clicked.connect(self.main_controller.open_ebay_window)