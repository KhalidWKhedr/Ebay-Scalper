from PySide6.QtWidgets import QDialog
from src.view.gui.gui_form_database import Ui_form_Database
from src.models.model_database_connection_details import SchemaConnectionDetails

class ConnectionSettingsPresenter:
    def __init__(
        self,
        ui: Ui_form_Database,
        schema_connection_details: SchemaConnectionDetails
    ):
        self.ui = ui
        self.schema_connection_details = schema_connection_details

    def load_connection_settings(self, connection_settings: dict) -> None:
        """Load connection settings into the UI or set defaults."""
        if connection_settings:
            self.set_ui_from_connection_settings(connection_settings)
        else:
            self.set_default_ui()

    def set_ui_from_connection_settings(self, connection_settings: dict) -> None:
        """Populate UI from connection settings."""
        self.ui.text_Host.setPlainText(connection_settings.get('MONGO_HOST', ''))
        self.ui.text_Port.setPlainText(connection_settings.get('MONGO_PORT', ''))
        self.ui.text_Username.setPlainText(connection_settings.get('MONGO_USER', ''))
        self.ui.text_Password.setPlainText(connection_settings.get('MONGO_PASSWORD', ''))
        self.ui.text_DbName.setPlainText(connection_settings.get('MONGO_DB_NAME', ''))
        self.ui.text_AuthSource.setPlainText(connection_settings.get('MONGO_AUTH_DB', ''))
        self.ui.text_SSH_Host.setPlainText(connection_settings.get('SSH_HOST', ''))
        self.ui.text_SSH_Port.setPlainText(connection_settings.get('SSH_PORT', ''))
        self.ui.text_SSH_Username.setPlainText(connection_settings.get('SSH_USERNAME', ''))
        self.ui.text_SSH_Password.setPlainText(connection_settings.get('SSH_PASSWORD', ''))

    def set_default_ui(self) -> None:
        """Set default UI values."""
        self.ui.text_Host.setPlainText("localhost")
        self.ui.text_Port.setPlainText("27017")
        self.ui.text_Username.setPlainText("")
        self.ui.text_Password.setPlainText("")
        self.ui.text_DbName.setPlainText("test_db")
        self.ui.text_AuthSource.setPlainText("admin")