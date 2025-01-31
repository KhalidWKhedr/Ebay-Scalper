from PySide6.QtWidgets import QDialog
from database.DatabaseService import DatabaseService
from services.NotificationService import NotificationService
from gui.gui_form_ebay import Ui_form_EbayAPI
from logger.LoggingService import LoggingService
from utils.converter import Converter

class EbayApiController(QDialog, Ui_form_EbayAPI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.notification_service = NotificationService()
        self.button_CONNECT.clicked.connect(self.connect_to_api())

    def connect_to_api(self):
        api_details = self.get_api_details()
        LoggingService.log(f"Attempting to connect to Ebay API at host: {api_details['host']}", level="info")

        try:
            message = self.db_service.connect(api_details)
            LoggingService.log(f"Connection to database successful: {message}", level="info")
        except Exception as e:
            LoggingService.log(f"Failed to connect to database: {str(e)}", level="error")

        self.notification_service.show_message(self, message)

    def get_api_details(self):
        """Collect and return all necessary connection details from the UI."""

        return {
            'api_app_id': self.text_AppID.toPlainText().strip(),
            'api_domain': self.text_Domain.toPlainText().strip(),
            "api_site_id": self.comboBox_SITE_ID.toPlainText().strip(),
        }