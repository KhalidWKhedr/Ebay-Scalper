from PySide6.QtWidgets import QDialog
from src.view.gui.gui_form_ebay import Ui_form_EbayAPI
from src.controllers.controller_ebay_api import EbayApiController

class EbayWindowPresenter(QDialog, Ui_form_EbayAPI):
    def __init__(
        self,
        notification_service,
        ebay_controller: EbayApiController
    ):
        super().__init__()
        self.setupUi(self)
        self.notification_service = notification_service
        self.ebay_controller = ebay_controller
        self.initialize_ui()

    def initialize_ui(self) -> None:
        """Initialize UI elements like combo boxes and set up signal connections."""
        self.text_Domain.setReadOnly(True)

        site_names = self.ebay_controller.site_domain_model.get_site_names()  # Use the model
        self.comboBox_SITE_ID.addItems(site_names)

        self.text_Domain.setPlainText(self.ebay_controller.get_connection_settings().get("API_DOMAIN", ""))
        self.text_AppID.setPlainText(self.ebay_controller.get_connection_settings().get("API_ID", ""))
        self.comboBox_SITE_ID.setCurrentText(self.ebay_controller.get_connection_settings().get("API_SITE_ID", ""))

        self.comboBox_SITE_ID.currentTextChanged.connect(self.update_domain_field)
        self.button_CONNECT.clicked.connect(self.connect_to_api)


    def update_domain_field(self, selected_country: str) -> None:
        """Update the domain field based on the selected country."""
        domain = self.ebay_controller.site_domain_model.get_domain_for_site(selected_country)  # Use the model
        if domain:
            self.text_Domain.setPlainText(domain)

    def connect_to_api(self) -> None:
        """Handle API connection attempt."""
        api_details = self.get_api_details()
        try:
            message = self.ebay_controller.connect_to_api(api_details)
            self.notification_service.show_message(self, message)
        except Exception as e:
            self.notification_service.show_message(self, f"Error: {str(e)}")

    def get_api_details(self) -> dict[str, str]:
        """Retrieve API details from UI inputs."""
        selected_site = self.comboBox_SITE_ID.currentText().strip()
        return {
            'API_ID': self.text_AppID.toPlainText().strip(),
            'API_DOMAIN': self.text_Domain.toPlainText().strip(),
            'API_SITE_ID': self.ebay_controller.site_domain_model.get_site_id_for_site_name(selected_site) or "",
        }