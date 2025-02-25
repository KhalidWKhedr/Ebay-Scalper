from src.view.gui.gui_form_database import Ui_form_Database

class ConnectionSettingsPresenter:
    def __init__(self, ui: Ui_form_Database):
        self.ui = ui

    def load_connection_settings(self, connection_settings: dict) -> None:
        """Load connection settings into the UI with defaults if missing."""
        defaults = {
            "MONGO_HOST": "localhost",
            "MONGO_PORT": "27017",
            "MONGO_USER": "",
            "MONGO_PASSWORD": "",
            "MONGO_DB_NAME": "test_db",
            "MONGO_AUTH_DB": "admin",
            "SSH_HOST": "",
            "SSH_PORT": "",
            "SSH_USERNAME": "",
            "SSH_PASSWORD": "",
            "SSH_TOGGLE": False
        }

        # Mapping of UI fields to dictionary keys
        ui_fields = {
            "text_Host": "MONGO_HOST",
            "text_Port": "MONGO_PORT",
            "text_Username": "MONGO_USER",
            "text_Password": "MONGO_PASSWORD",
            "text_DbName": "MONGO_DB_NAME",
            "text_AuthSource": "MONGO_AUTH_DB",
            "text_SSH_Host": "SSH_HOST",
            "text_SSH_Port": "SSH_PORT",
            "text_SSH_Username": "SSH_USERNAME",
            "text_SSH_Password": "SSH_PASSWORD"
        }

        # Set UI fields dynamically
        for field, key in ui_fields.items():
            getattr(self.ui, field).setPlainText(connection_settings.get(key, defaults[key]))

        # Handle checkbox separately
        self.ui.checkbox_SSH.setChecked(str(connection_settings.get("SSH_TOGGLE", "False")).lower() in ["true", "1"])
