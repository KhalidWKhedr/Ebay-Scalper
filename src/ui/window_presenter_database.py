from PySide6.QtWidgets import QDialog
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

    def initialize_ui(self):
        """Initialize UI and load connection settings."""
        connection_settings = self.database_controller.get_connection_settings()
        if connection_settings:
            self.set_ui_from_connection_settings(connection_settings)
        else:
            self.set_default_ui()

        self.set_authentication_radio(self.schema_connection_details.auth_type)
        self.update_mongo_uri()
        self.setup_connections()

    def set_ui_from_connection_settings(self, connection_settings):
        """Populate UI from connection settings."""
        self.text_Host.setPlainText(connection_settings['host'])
        self.text_Port.setPlainText(str(connection_settings['port']))
        self.text_Username.setPlainText(connection_settings['user'])
        self.text_Password.setPlainText(connection_settings['password'])
        self.text_DbName.setPlainText(connection_settings['db_name'])
        self.text_AuthSource.setPlainText(connection_settings['auth_source'])
        self.text_SSH_Host.setPlainText(connection_settings['ssh_host'])
        self.text_SSH_Port.setPlainText(str(connection_settings['ssh_port']))
        self.text_SSH_Username.setPlainText(connection_settings['ssh_username'])
        self.text_SSH_Password.setPlainText(connection_settings['ssh_password'])

    def set_default_ui(self):
        """Set default UI values."""
        self.text_Host.setPlainText("localhost")
        self.text_Port.setPlainText("27017")
        self.text_Username.setPlainText("")
        self.text_Password.setPlainText("")
        self.text_DbName.setPlainText("test_db")
        self.text_AuthSource.setPlainText("admin")

    def setup_connections(self):
        """Setup signal-slot connections."""
        self.checkbox_SSH.toggled.connect(self.toggle_ssh_options)
        self.button_Connect.clicked.connect(self.connect_to_db)
        self.setup_text_changed_connections()
        self.setup_radio_button_connections()
        self.toggle_ssh_options(self.checkbox_SSH.isChecked())

    def setup_text_changed_connections(self):
        """Setup text change connections to update Mongo URI."""
        text_fields = [
            self.text_SSH_Host, self.text_SSH_Port, self.text_SSH_Username,
            self.text_SSH_Password, self.text_Host, self.text_Port,
            self.text_Username, self.text_Password, self.text_DbName,
            self.text_AuthSource
        ]
        for field in text_fields:
            field.textChanged.connect(self.update_mongo_uri)

    def setup_radio_button_connections(self):
        """Connect radio buttons to update auth type dynamically."""
        radio_buttons = [
            self.radio_X509, self.radio_SHA1, self.radio_AWS,
            self.radio_KERBEROS_2, self.radio_SHA256, self.radio_KERBEROS,
            self.radio_LDAP
        ]
        for button in radio_buttons:
            button.toggled.connect(self.update_mongo_uri)

    def set_authentication_radio(self, auth_type):
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

    def update_mongo_uri(self):
        """Generate Mongo URI based on user input."""
        uri = self.build_mongo_uri()
        self.text_MongoUri.setPlainText(uri)

    def build_mongo_uri(self):
        """Build Mongo URI from the connection details stored in schema."""
        connection_details = self.schema_connection_details.model_dump()
        print(connection_details.get('host'))
        uri = f"mongodb://{connection_details.get('user')}:{connection_details.get('password')}@" \
              f"{connection_details.get('host')}:{connection_details.get('port')}/" \
              f"{connection_details.get('db_name')}?authSource={connection_details.get('auth_source')}"
        if connection_details.get('auth_type'):
            uri += f"&authMechanism={connection_details.get('auth_type')}"
        return uri

    def get_connection_details(self) -> SchemaConnectionDetails:
        """Extract UI data and create a Pydantic model."""
        return SchemaConnectionDetails(
            use_ssh=self.checkbox_SSH.isChecked(),
            host=self.text_Host.toPlainText().strip(),
            port=self.text_Port.toPlainText().strip(),
            user=self.text_Username.toPlainText().strip(),
            password=self.text_Password.toPlainText().strip(),
            db_name=self.text_DbName.toPlainText().strip(),
            auth_source=self.text_AuthSource.toPlainText().strip(),
            ssh_host=self.text_SSH_Host.toPlainText().strip(),
            ssh_port=self.text_SSH_Port.toPlainText().strip(),
            ssh_username=self.text_SSH_Username.toPlainText().strip(),
            ssh_password=self.text_SSH_Password.toPlainText().strip(),
            auth_type=self.get_selected_auth_type(),
        )

    def get_selected_auth_type(self):
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

    def toggle_ssh_options(self, is_checked):
        """Toggle visibility of SSH options based on checkbox."""
        ssh_elements = [
            self.text_SSH_Host, self.text_SSH_Port, self.text_SSH_Username,
            self.text_SSH_Password, self.label_ssh_host, self.label_ssh_port,
            self.label_ssh_username, self.label_ssh_password
        ]
        for element in ssh_elements:
            element.setVisible(is_checked)

    def connect_to_db(self):
        """Attempt to connect to the database."""
        connection_details = self.get_connection_details()
        try:
            message = self.database_controller.connect_to_db(connection_details)
            self.database_controller.notification_service.show_message(self, message)
        except Exception as e:
            self.database_controller.notification_service.show_message(self, str(e))
