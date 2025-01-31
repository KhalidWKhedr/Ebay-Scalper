from PySide6.QtWidgets import QDialog
from services.ebay.EbayService import EbayService
from services.NotificationService import NotificationService
from gui.gui_form_ebay import Ui_form_EbayAPI
from logger.LoggingService import LoggingService
from services.ebay.EbaySites import EBAY_SITES  # Import the site mappings


class EbayApiController(QDialog, Ui_form_EbayAPI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ebay_service = EbayService()
        self.notification_service = NotificationService()

        self.ebay_sites = EBAY_SITES
        self.initialize_ui()

    def initialize_ui(self):
        """Setup UI elements like the eBay site combo box."""
        self.comboBox_SITE_ID.addItems(self.ebay_sites.keys())
        self.button_CONNECT.clicked.connect(self.connect_to_api)

    def get_site_code(self, site_name):
        """Retrieve eBay site code based on the selected site name."""
        return self.ebay_sites.get(site_name, "")

    def connect_to_api(self):
        """Handle the API connection process."""
        api_details = self.get_api_details()
        LoggingService.log(f"Attempting to connect to eBay API with details: {api_details}", level="info")

        try:
            message = self.ebay_service.connect(api_details)
            LoggingService.log(f"Connection to eBay API successful: {message}", level="info")
            self.notification_service.show_message(self, message)
        except Exception as e:
            error_message = f"Failed to connect to eBay API: {str(e)}"
            LoggingService.log(error_message, level="error")
            self.notification_service.show_message(self, error_message)

    def get_api_details(self):
        """Retrieve API details from UI inputs."""
        selected_country = self.comboBox_SITE_ID.currentText().strip()
        return {
            'api_id': self.text_AppID.toPlainText().strip(),
            'api_domain': self.text_Domain.toPlainText().strip(),
            'api_site_id': self.get_site_code(selected_country),
        }
