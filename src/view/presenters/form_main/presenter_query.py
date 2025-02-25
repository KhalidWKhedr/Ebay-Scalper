from src.controllers import EbayController


class QueryPresenter:
    def __init__(
        self,
        ebay_controller: EbayController,
        notification_service
    ):
        self.main_window = None  # Initialize as None
        self.ebay_controller = ebay_controller
        self.notification_service = notification_service

    def set_main_window(self, main_window):
        """Sets the main window for the presenter."""
        self.main_window = main_window
        self._connect_ui_actions()  # Connect UI actions after main_window is set

    def _connect_ui_actions(self):
        """Connects UI actions to their respective methods."""
        self.main_window.main_ui.button_EbaySearch.clicked.connect(
            lambda: self.ebay_controller.test_connection(
                api_details=self.ebay_controller.get_saved_connection_settings()
            )
        )
