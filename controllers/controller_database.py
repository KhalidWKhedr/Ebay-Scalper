from PySide6.QtWidgets import QDialog
from database.service_database import DatabaseService
from services.service_notification import NotificationService
from gui.gui_form_database import Ui_form_Database
from logger.service_logging import LoggingService
from utils.converter import Converter

class DatabaseController(QDialog, Ui_form_Database):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_service = DatabaseService()
        self.notification_service = NotificationService()

        self.initialize_ui()

        # Radio button connections
        self.checkbox_SSH.toggled.connect(self.toggle_ssh_options)
        self.button_Connect.clicked.connect(self.connect_to_db)

        # Connect UI elements for textChanged
        self.text_SSH_Host.textChanged.connect(self.update_mongo_uri)
        self.text_SSH_Port.textChanged.connect(self.update_mongo_uri)
        self.text_SSH_Username.textChanged.connect(self.update_mongo_uri)
        self.text_SSH_Password.textChanged.connect(self.update_mongo_uri)
        self.text_Host.textChanged.connect(self.update_mongo_uri)
        self.text_Port.textChanged.connect(self.update_mongo_uri)
        self.text_Username.textChanged.connect(self.update_mongo_uri)
        self.text_Password.textChanged.connect(self.update_mongo_uri)
        self.text_DbName.textChanged.connect(self.update_mongo_uri)
        self.text_AuthSource.textChanged.connect(self.update_mongo_uri)

        # Connect radio buttons to update auth type dynamically
        self.radio_X509.toggled.connect(self.update_mongo_uri)
        self.radio_SHA1.toggled.connect(self.update_mongo_uri)
        self.radio_AWS.toggled.connect(self.update_mongo_uri)
        self.radio_KERBEROS_2.toggled.connect(self.update_mongo_uri)
        self.radio_SHA256.toggled.connect(self.update_mongo_uri)
        self.radio_KERBEROS.toggled.connect(self.update_mongo_uri)
        self.radio_LDAP.toggled.connect(self.update_mongo_uri)

        self.toggle_ssh_options(self.checkbox_SSH.isChecked())

    def initialize_ui(self):
        """Setup UI elements based on saved connection settings."""
        connection_settings = self.db_service.get_connection_settings()

        if connection_settings:
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
            self.set_authentication_radio(connection_settings['auth_type'])

        else:
            self.text_Host.setPlainText("localhost")
            self.text_Port.setPlainText("27017")
            self.text_Username.setPlainText("")
            self.text_Password.setPlainText("")
            self.text_DbName.setPlainText("test_db")
            self.text_AuthSource.setPlainText("admin")

        self.set_authentication_radio(connection_settings['auth_type'])

        self.text_MongoUri.setPlainText(
            f"mongodb://{connection_settings['user'].replace('@', '%40')}:"
            f"{connection_settings['password'].replace('@', '%40')}@"
            f"{connection_settings['host']}:{connection_settings['port']}/"
            f"{connection_settings['db_name']}?"
            f"authSource={connection_settings['auth_source']}&authMechanism={connection_settings['auth_type']}"
        )

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
        host = self.text_Host.toPlainText().strip()
        port = self.text_Port.toPlainText().strip()
        user = self.text_Username.toPlainText().strip().replace("@", "%40")
        password = self.text_Password.toPlainText().strip().replace("@", "%40")
        db_name = self.text_DbName.toPlainText().strip()
        auth_source = self.text_AuthSource.toPlainText().strip()

        auth_map = {
            self.radio_X509: "MONGODB-X509",
            self.radio_SHA1: "SCRAM-SHA-1",
            self.radio_AWS: "MONGODB-AWS",
            self.radio_KERBEROS_2: "PLAIN",
            self.radio_SHA256: "SCRAM-SHA-256",
            self.radio_KERBEROS: "GSSAPI (Kerberos)",
            self.radio_LDAP: "LDAP"
        }

        auth_type = None
        for radio_button, auth_value in auth_map.items():
            if radio_button.isChecked():
                auth_type = auth_value
                break

        uri = f"mongodb://{user}:{password}@{host}:{port}/{db_name}?authSource={auth_source}"
        if auth_type:
            uri += f"&authMechanism={auth_type}"

        self.text_MongoUri.setPlainText(uri)

    def connect_to_db(self):
        connection_details = self.get_connection_details()
        LoggingService.log(f"Attempting to connect to database at host: {connection_details['host']}", level="info")

        try:
            message = self.db_service.connect(connection_details)
            self.db_service.save_connection_settings(connection_details)
            data = self.db_service.get_connection_settings()

            LoggingService.log(f"Connection to database successful: {message}", level="info")
        except Exception as e:
            LoggingService.log(f"Failed to connect to database: {str(e)}", level="error")

        self.notification_service.show_message(self, message)

    def get_connection_details(self):
        """Collect and return all necessary connection details from the UI."""
        auth_type = self.get_selected_auth_type()

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
            'auth_type': auth_type,
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

    def toggle_ssh_options(self, is_checked):
        """Toggle the visibility of SSH-related options based on checkbox state."""
        self.text_SSH_Host.setVisible(is_checked)
        self.text_SSH_Port.setVisible(is_checked)
        self.text_SSH_Username.setVisible(is_checked)
        self.text_SSH_Password.setVisible(is_checked)
        self.label_ssh_host.setVisible(is_checked)
        self.label_ssh_port.setVisible(is_checked)
        self.label_ssh_username.setVisible(is_checked)
        self.label_ssh_password.setVisible(is_checked)