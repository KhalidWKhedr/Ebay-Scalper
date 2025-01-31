from PySide6.QtWidgets import QDialog
from services.ebay.EbayService import EbayService
from services.NotificationService import NotificationService
from gui.gui_form_ebay import Ui_form_EbayAPI
from logger.LoggingService import LoggingService

class EbayApiController(QDialog, Ui_form_EbayAPI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ebay_service = EbayService()
        self.notification_service = NotificationService()
        self.button_CONNECT.clicked.connect(self.connect_to_api)  # FIXED

    def connect_to_api(self):
        api_details = self.get_api_details()
        LoggingService.log(f"Attempting to connect to eBay API with details: {api_details}", level="info")
        try:
            message = self.ebay_service.connect(api_details)
            LoggingService.log(f"Connection to eBay API successful: {message}", level="info")
        except Exception as e:
            LoggingService.log(f"Failed to connect to eBay API: {str(e)}", level="error")

        self.notification_service.show_message(self, message)

    def get_api_details(self):
        return {
            'api_id': self.text_AppID.toPlainText().strip(),
            'api_domain': self.text_Domain.toPlainText().strip(),
            'api_site_id': self.comboBox_SITE_ID.toPlainText().strip(),
        }
