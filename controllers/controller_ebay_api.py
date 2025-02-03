from PySide6.QtWidgets import QDialog
from services.ebay.service_ebay import EbayService
from services.service_notification import NotificationService
from gui.gui_form_ebay import Ui_form_EbayAPI
from logger.service_logging import LoggingService
from services.ebay.ebay_site_domain import SITE_DOMAIN_MAPPING


class EbayApiController(QDialog, Ui_form_EbayAPI):
    def __init__(self, ebay_service: EbayService, notification_service: NotificationService,
                 site_domain_mapping: dict = SITE_DOMAIN_MAPPING):
        super().__init__()
        self.setupUi(self)

        self.ebay_service = ebay_service
        self.notification_service = notification_service
        self.site_domain_mapping = site_domain_mapping

        self.initialize_ui()

    def initialize_ui(self):
        """Setup UI elements like the eBay site combo box."""
        self.comboBox_SITE_ID.addItems(self.site_domain_mapping.keys())
        self.text_Domain.setPlainText(next(iter(self.site_domain_mapping.values()))["domain"])
        self.comboBox_SITE_ID.currentTextChanged.connect(self.update_domain_field)
        self.button_CONNECT.clicked.connect(self.connect_to_api)
        self.text_Domain.setReadOnly(True)

    def update_domain_field(self, selected_site_id):
        """Update the domain field based on the selected site ID."""
        site_info = self.site_domain_mapping.get(selected_site_id, {})
        domain = site_info.get('domain', '')
        self.text_Domain.setPlainText(domain)

    def get_site_code(self, site_name):
        """Retrieve eBay site code based on the selected site name."""
        return self.site_domain_mapping.get(site_name, {}).get('site', "")

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
