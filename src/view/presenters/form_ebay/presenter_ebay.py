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

        # Get site names and populate the combo box
        site_names = self.ebay_controller.site_domain_model.get_site_names()  # Use the model
        self.comboBox_SITE_ID.addItems(site_names)

        # Set initial text fields with saved connection settings
        connection_settings = self.ebay_controller.get_saved_connection_settings()
        self.text_Domain.setPlainText(connection_settings.get("API_DOMAIN", ""))
        self.text_AppID.setPlainText(connection_settings.get("API_ID", ""))

        # Get the saved API_SITE_ID
        api_site_id = connection_settings.get("API_SITE_ID", "")

        # Get the country name from the saved API_SITE_ID
        country = self.ebay_controller.site_domain_model.get_country_from_site_id(api_site_id)

        # Find the country name in the combo box and set the current index if found
        if country:
            index = self.comboBox_SITE_ID.findText(country)
            if index >= 0:
                self.comboBox_SITE_ID.setCurrentIndex(index)
            else:
                # Optional: Handle case where the country wasn't found in the combo box
                print(f"Country {country} not found in combo box.")

        # Connect signals to slots
        self.comboBox_SITE_ID.currentTextChanged.connect(self.update_domain_field)
        self.button_TestApi.clicked.connect(self.test_api_connection)
        self.button_SaveApiSettings.clicked.connect(self.save_api_details)

    def update_domain_field(self, selected_country: str) -> None:
        """Update the domain field based on the selected country."""
        domain = self.ebay_controller.site_domain_model.get_domain_for_site(selected_country)  # Use the model
        if domain:
            self.text_Domain.setPlainText(domain)
        else:
            # Optional: Handle case where no domain is found
            print(f"No domain found for {selected_country}.")

    def test_api_connection(self) -> None:
        """Handle API connection attempt."""
        api_details = self.get_api_details()
        try:
            message = self.ebay_controller.test_connection(api_details)
            self.notification_service.show_message(self, message)
        except Exception as e:
            self.notification_service.show_message(self, f"Error: {str(e)}")

    def save_api_details(self) -> None:
        """Save API details."""
        api_details = self.get_api_details()
        print(api_details)
        try:
            message = self.ebay_controller.save_connection_settings(api_details)
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