class ConnectionSettingsPresenter:
    """Handles loading connection settings into the UI."""

    def __init__(
        self,
        host_field, port_field, username_field, password_field,
        db_name_field, auth_source_field, ssh_host_field, ssh_port_field,
        ssh_username_field, ssh_password_field, ssh_checkbox
    ):
        self.host_field = host_field
        self.port_field = port_field
        self.username_field = username_field
        self.password_field = password_field
        self.db_name_field = db_name_field
        self.auth_source_field = auth_source_field
        self.ssh_host_field = ssh_host_field
        self.ssh_port_field = ssh_port_field
        self.ssh_username_field = ssh_username_field
        self.ssh_password_field = ssh_password_field
        self.ssh_checkbox = ssh_checkbox

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
            self.host_field: "MONGO_HOST",
            self.port_field: "MONGO_PORT",
            self.username_field: "MONGO_USER",
            self.password_field: "MONGO_PASSWORD",
            self.db_name_field: "MONGO_DB_NAME",
            self.auth_source_field: "MONGO_AUTH_DB",
            self.ssh_host_field: "SSH_HOST",
            self.ssh_port_field: "SSH_PORT",
            self.ssh_username_field: "SSH_USERNAME",
            self.ssh_password_field: "SSH_PASSWORD"
        }

        # Set UI fields dynamically
        for field, key in ui_fields.items():
            field.setPlainText(connection_settings.get(key, defaults[key]))

        # Handle checkbox separately
        self.ssh_checkbox.setChecked(str(connection_settings.get("SSH_TOGGLE", "False")).lower() in ["true", "1"])