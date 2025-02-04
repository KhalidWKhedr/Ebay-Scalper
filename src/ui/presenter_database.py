from PySide6.QtWidgets import QDialog, QMessageBox
from gui.gui_form_database import Ui_form_Database
from src.controllers.controller_database import DatabaseController
from src.models.model_database_connection_details import SchemaConnectionDetails


class DatabaseWindowPresenter(QDialog, Ui_form_Database):
    def __init__(self, database_controller: DatabaseController,
                 schema_connection_details: SchemaConnectionDetails):
        super().__init__()
        self.setupUi(self)
        self.database_controller = database_controller
        self.schema_connection_details = schema_connection_details
        self.initialize_ui()

    def initialize_ui(self) -> None:
        """Initialize UI and load connection settings."""
        self.load_connection_settings()
        self.set_authentication_radio(self.schema_connection_details.AUTH_TYPE)
        self.update_mongo_uri()
        self.setup_connections()

    def load_connection_settings(self) -> None:
        """Load connection settings into the UI or set defaults."""
        connection_settings = self.database_controller.get_connection_settings()
        if connection_settings:
            self.set_ui_from_connection_settings(connection_settings)
        else:
            self.set_default_ui()

    def set_ui_from_connection_settings(self, connection_settings: dict) -> None:
        """Populate UI from connection settings."""
        self.text_Host.setPlainText(connection_settings.get('MONGO_HOST', ''))
        self.text_Port.setPlainText(connection_settings.get('MONGO_PORT', ''))
        self.text_Username.setPlainText(connection_settings.get('MONGO_USER', ''))
        self.text_Password.setPlainText(connection_settings.get('MONGO_PASSWORD', ''))
        self.text_DbName.setPlainText(connection_settings.get('MONGO_DB_NAME', ''))
        self.text_AuthSource.setPlainText(connection_settings.get('MONGO_AUTH_DB', ''))
        self.text_SSH_Host.setPlainText(connection_settings.get('SSH_HOST', ''))
        self.text_SSH_Port.setPlainText(connection_settings.get('SSH_PORT', ''))
        self.text_SSH_Username.setPlainText(connection_settings.get('SSH_USERNAME', ''))
        self.text_SSH_Password.setPlainText(connection_settings.get('SSH_PASSWORD', ''))

    def set_default_ui(self) -> None:
        """Set default UI values."""
        self.text_Host.setPlainText("localhost")
        self.text_Port.setPlainText("27017")
        self.text_Username.setPlainText("")
        self.text_Password.setPlainText("")
        self.text_DbName.setPlainText("test_db")
        self.text_AuthSource.setPlainText("admin")

    def setup_connections(self) -> None:
        """Setup signal-slot connections."""
        self.checkbox_SSH.toggled.connect(self.toggle_ssh_options)
        self.button_Connect.clicked.connect(self.connect_to_db)
        self.setup_text_changed_connections()
        self.setup_radio_button_connections()
        self.toggle_ssh_options(self.checkbox_SSH.isChecked())

    def setup_text_changed_connections(self) -> None:
        """Setup text change connections to update Mongo URI."""
        text_fields = [
            self.text_SSH_Host, self.text_SSH_Port, self.text_SSH_Username,
            self.text_SSH_Password, self.text_Host, self.text_Port,
            self.text_Username, self.text_Password, self.text_DbName,
            self.text_AuthSource
        ]
        for field in text_fields:
            field.textChanged.connect(self.update_mongo_uri)

    def setup_radio_button_connections(self) -> None:
        """Connect radio buttons to update auth type dynamically."""
        radio_buttons = [
            self.radio_X509, self.radio_SHA1, self.radio_AWS,
            self.radio_KERBEROS_2, self.radio_SHA256, self.radio_KERBEROS,
            self.radio_LDAP
        ]
        for button in radio_buttons:
            button.toggled.connect(self.update_mongo_uri)

    def set_authentication_radio(self, auth_type: str) -> None:
        """Set the appropriate radio button for authentication type."""
        auth_map = {
            "MONGODB-X509": self.radio_X509,
            "SCRAM-SHA-1": self.radio_SHA1,
            "MONGODB-AWS": self.radio_AWS,
            "PLAIN": self.radio_KERBEROS_2,
            "SCRAM-SHA-256": self.radio_SHA256,
            "GSSAPI (Kerberos)": self.radio_KERBEROS,
            "LDAP": self.radio_LDAP
        }

        for radio_button in auth_map.values():
            radio_button.setChecked(False)

        if auth_type and auth_type in auth_map:
            auth_map[auth_type].setChecked(True)

    def update_mongo_uri(self) -> None:
        """Generate Mongo URI based on user input."""
        uri = self.build_mongo_uri()
        self.text_MongoUri.setPlainText(uri)

    def build_mongo_uri(self) -> str:
        """Build Mongo URI from the connection details stored in schema."""
        connection_details = self.get_connection_details()
        uri = f"mongodb://{connection_details.MONGO_USER}:{connection_details.MONGO_PASSWORD}@" \
              f"{connection_details.MONGO_HOST}:{str(connection_details.MONGO_PORT)}/" \
              f"{connection_details.MONGO_DB_NAME}?authSource={connection_details.MONGO_AUTH_DB}"
        if connection_details.AUTH_TYPE:
            uri += f"&authMechanism={connection_details.AUTH_TYPE}"
        return uri

    def get_connection_details(self) -> SchemaConnectionDetails:
        """Extract UI data and create a Pydantic model."""
        return SchemaConnectionDetails(
            SSH_TOGGLE=self.checkbox_SSH.isChecked(),
            MONGO_HOST=self.text_Host.toPlainText().strip(),
            MONGO_PORT=self.text_Port.toPlainText().strip(),
            MONGO_USER=self.text_Username.toPlainText().strip(),
            MONGO_PASSWORD=self.text_Password.toPlainText().strip(),
            MONGO_DB_NAME=self.text_DbName.toPlainText().strip(),
            MONGO_AUTH_DB=self.text_AuthSource.toPlainText().strip(),
            SSH_HOST=self.text_SSH_Host.toPlainText().strip(),
            SSH_PORT=self.text_SSH_Port.toPlainText().strip(),
            SSH_USERNAME=self.text_SSH_Username.toPlainText().strip(),
            SSH_PASSWORD=self.text_SSH_Password.toPlainText().strip(),
            AUTH_TYPE=self.get_selected_auth_type(),
        )

    def get_selected_auth_type(self) -> str | None:
        """Get the selected authentication type from radio buttons."""
        auth_map = {
            self.radio_X509: "MONGODB-X509",
            self.radio_SHA1: "SCRAM-SHA-1",
            self.radio_AWS: "MONGODB-AWS",
            self.radio_KERBEROS_2: "PLAIN",
            self.radio_SHA256: "SCRAM-SHA-256",
            self.radio_KERBEROS: "GSSAPI (Kerberos)",
            self.radio_LDAP: "LDAP"
        }

        for radio_button, auth_value in auth_map.items():
            if radio_button.isChecked():
                return auth_value

        return None

    def toggle_ssh_options(self, is_checked: bool) -> None:
        """Toggle visibility of SSH options based on checkbox."""
        ssh_elements = [
            self.text_SSH_Host, self.text_SSH_Port, self.text_SSH_Username,
            self.text_SSH_Password, self.label_ssh_host, self.label_ssh_port,
            self.label_ssh_username, self.label_ssh_password
        ]
        for element in ssh_elements:
            element.setVisible(is_checked)

    def connect_to_db(self, connection_details):
        """Attempt to connect to the database and show appropriate messages."""
        result = self.database_controller.connect_to_db(self.get_connection_details())

        if result == "Connection successful":
            QMessageBox.information(
                self,  # Use 'self' as the parent widget
                "Database Connection",
                "Database connection successful!"
            )
        else:
            QMessageBox.critical(
                self,  # Use 'self' as the parent widget
                "Database Connection Error",
                result
            )