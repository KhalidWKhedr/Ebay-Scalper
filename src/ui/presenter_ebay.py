from PySide6.QtWidgets import QDialog
from gui.gui_form_ebay import Ui_form_EbayAPI
from src.controllers.controller_ebay_api import EbayApiController


class EbayWindowPresenter(QDialog, Ui_form_EbayAPI):
    def __init__(self, ebay_controller: EbayApiController):
        super().__init__()
        self.setupUi(self)
        self.ebay_controller = ebay_controller
        self.initialize_ui()

    def initialize_ui(self) -> None:
        """Initialize UI elements like combo boxes and set up signal connections."""
        self.comboBox_SITE_ID.addItems(self.get_available_sites())
        self.text_Domain.setPlainText(self.get_default_domain())
        self.comboBox_SITE_ID.currentTextChanged.connect(self.update_domain_field)
        self.button_CONNECT.clicked.connect(self.connect_to_api)
        self.text_Domain.setReadOnly(True)

    def update_domain_field(self, selected_site_id: str) -> None:
        """Update the domain field based on the selected site ID."""
        domain = self.ebay_controller.get_domain_for_site(selected_site_id)
        self.text_Domain.setPlainText(domain)

    def connect_to_api(self) -> None:
        """Handle API connection attempt."""
        api_details = self.get_api_details()
        try:
            message = self.ebay_controller.connect_to_api(api_details)
            self.ebay_controller.notification_service.show_message(self, message)
        except Exception as e:
            self.ebay_controller.notification_service.show_message(self, f"Error: {str(e)}")
            self.ebay_controller.logger.error(f"Failed to connect to API: {e}")

    def get_api_details(self) -> dict[str, str]:
        """Retrieve API details from UI inputs."""
        selected_site = self.comboBox_SITE_ID.currentText().strip()
        return {
            'api_id': self.text_AppID.toPlainText().strip(),
            'api_domain': self.text_Domain.toPlainText().strip(),
            'api_site_id': self.ebay_controller.get_site_code(selected_site),
        }

    def get_available_sites(self) -> list[str]:
        """Retrieve list of available sites from the controller."""
        return list(self.ebay_controller.site_domain_mapping.keys())

    def get_default_domain(self) -> str:
        """Get the default domain from the controller."""
        if not self.ebay_controller.site_domain_mapping:
            return ""
        return next(iter(self.ebay_controller.site_domain_mapping.values()))["domain"]