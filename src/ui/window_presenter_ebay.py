from PySide6.QtWidgets import QDialog

from gui.gui_form_ebay import Ui_form_EbayAPI
from src.controllers.controller_ebay_api import EbayApiController


class EbayWindowPresenter(QDialog, Ui_form_EbayAPI):
    def __init__(self, ebay_controller: EbayApiController):
        super().__init__()
        self.setupUi(self)
        self.ebay_controller = ebay_controller

        self.initialize_ui()

    def initialize_ui(self):
        """Setup UI elements like the eBay site combo box."""
        self.comboBox_SITE_ID.addItems(self.ebay_controller.site_domain_mapping.keys())
        self.text_Domain.setPlainText(next(iter(self.ebay_controller.site_domain_mapping.values()))["domain"])
        self.comboBox_SITE_ID.currentTextChanged.connect(self.update_domain_field)
        self.button_CONNECT.clicked.connect(self.connect_to_api)
        self.text_Domain.setReadOnly(True)

    def update_domain_field(self, selected_site_id):
        """Update the domain field based on the selected site ID."""
        site_info = self.ebay_controller.site_domain_mapping.get(selected_site_id, {})
        domain = site_info.get('domain', '')
        self.text_Domain.setPlainText(domain)

    def connect_to_api(self):
        """Handle the API connection process."""
        api_details = self.get_api_details()
        try:
            message = self.ebay_controller.connect_to_api(api_details)
            self.ebay_controller.notification_service.show_message(self, message)
        except Exception as e:
            self.ebay_controller.notification_service.show_message(self, str(e))

    def get_api_details(self):
        """Retrieve API details from UI inputs."""
        selected_country = self.comboBox_SITE_ID.currentText().strip()
        return {
            'api_id': self.text_AppID.toPlainText().strip(),
            'api_domain': self.text_Domain.toPlainText().strip(),
            'api_site_id': self.ebay_controller.get_site_code(selected_country),
        }