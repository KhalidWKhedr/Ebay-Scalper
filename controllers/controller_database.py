from PySide6.QtWidgets import QDialog

from database.service_database import DatabaseService
from gui.gui_form_database import Ui_form_Database
from logger.service_logging import LoggingService
from services.service_notification import NotificationService
from utils.converter import Converter

class DatabaseController(QDialog, Ui_form_Database):
    def __init__(self, db_service: DatabaseService, logger: LoggingService,
                 converter: Converter, notification_service: NotificationService):
        super().__init__()
        self.setupUi(self)
        self.db_service = db_service
        self.logger = logger
        self.converter = converter
        self.notification_service = notification_service
        self.initialize_ui()

        # Connect UI elements to methods
        self.setup_connections()

    def initialize_ui(self):
        """Initialize the UI based on saved connection settings."""
        connection_settings = self.db_service.get_connection_settings()

        if connection_settings:
            self.set_ui_from_connection_settings(connection_settings)
        else:
            self.set_default_ui()

        self.set_authentication_radio(connection_settings.get('auth_type'))

        self.update_mongo_uri()

    def set_ui_from_connection_settings(self, connection_settings):
        """Populate the UI with the saved connection settings."""
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
        """Set default values for the UI elements."""
        self.text_Host.setPlainText("localhost")
        self.text_Port.setPlainText("27017")
        self.text_Username.setPlainText("")
        self.text_Password.setPlainText("")
        self.text_DbName.setPlainText("test_db")
        self.text_AuthSource.setPlainText("admin")

    def setup_connections(self):
        """Setup signal-slot connections for the UI elements."""
        self.checkbox_SSH.toggled.connect(self.toggle_ssh_options)
        self.button_Connect.clicked.connect(self.connect_to_db)

        # Connect text changes to update Mongo URI
        self.setup_text_changed_connections()

        # Connect radio buttons to update auth type dynamically
        self.setup_radio_button_connections()

        # Initialize SSH options visibility
        self.toggle_ssh_options(self.checkbox_SSH.isChecked())

    def setup_text_changed_connections(self):
        """Connect text changes to the update_mongo_uri method."""
        text_fields = [
            self.text_SSH_Host, self.text_SSH_Port, self.text_SSH_Username,
            self.text_SSH_Password, self.text_Host, self.text_Port,
            self.text_Username, self.text_Password, self.text_DbName,
            self.text_AuthSource
        ]
        for field in text_fields:
            field.textChanged.connect(self.update_mongo_uri)

    def setup_radio_button_connections(self):
        """Connect radio button toggles to the update_mongo_uri method."""
        radio_buttons = [
            self.radio_X509, self.radio_SHA1, self.radio_AWS,
            self.radio_KERBEROS_2, self.radio_SHA256, self.radio_KERBEROS,
            self.radio_LDAP
        ]
        for button in radio_buttons:
            button.toggled.connect(self.update_mongo_uri)

    def set_authentication_radio(self, auth_type):
        """Set the appropriate radio button based on the saved authentication type."""
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
        """Generate and update the MongoDB URI dynamically."""
        connection_details = self.get_connection_details()
        uri = f"mongodb://{connection_details['user']}:{connection_details['password']}@" \
              f"{connection_details['host']}:{connection_details['port']}/" \
              f"{connection_details['db_name']}?authSource={connection_details['auth_source']}"

        if connection_details['auth_type']:
            uri += f"&authMechanism={connection_details['auth_type']}"

        self.text_MongoUri.setPlainText(uri)

    def get_connection_details(self):
        """Collect and return all necessary connection details from the UI."""
        return {
            'use_ssh': self.checkbox_SSH.isChecked(),
            'host': self.text_Host.toPlainText().strip(),
            'port': Converter.safe_int_conversion(self.text_Port.toPlainText()) or None,
            'user': self.text_Username.toPlainText().strip(),
            'password': self.text_Password.toPlainText().strip(),
            'db_name': self.text_DbName.toPlainText().strip(),
            'auth_source': self.text_AuthSource.toPlainText().strip(),
            'ssh_host': self.text_SSH_Host.toPlainText().strip(),
            'ssh_port': Converter.safe_int_conversion(self.text_SSH_Port.toPlainText()) or None,
            'ssh_username': self.text_SSH_Username.toPlainText().strip(),
            'ssh_password': self.text_SSH_Password.toPlainText().strip(),
            'auth_type': self.get_selected_auth_type(),
        }

    def get_selected_auth_type(self):
        """Get the selected authentication type from the radio buttons."""
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

    def connect_to_db(self):
        """Attempt to connect to the database and log the result."""
        connection_details = self.get_connection_details()
        LoggingService.log(f"Attempting to connect to database at host: {connection_details['host']}", level="info")

        try:
            message = self.db_service.connect(connection_details)
            self.db_service.save_connection_settings(connection_details)
            LoggingService.log(f"Connection to database successful: {message}", level="info")
        except Exception as e:
            message = f"Failed to connect to database: {str(e)}"
            LoggingService.log(message, level="error")

        self.notification_service.show_message(self, message)

    def toggle_ssh_options(self, is_checked):
        """Toggle the visibility of SSH-related options based on checkbox state."""
        ssh_elements = [
            self.text_SSH_Host, self.text_SSH_Port, self.text_SSH_Username,
            self.text_SSH_Password, self.label_ssh_host, self.label_ssh_port,
            self.label_ssh_username, self.label_ssh_password
        ]
        for element in ssh_elements:
            element.setVisible(is_checked)
