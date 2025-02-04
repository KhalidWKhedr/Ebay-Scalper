class DatabaseUIManager:
    def __init__(self, database_service, schema_connection_details, form_ui):
        self.database_service = database_service
        self.schema_connection_details = schema_connection_details
        self.form_ui = form_ui

    def initialize_ui(self):
        """Initialize UI and load connection settings."""
        connection_settings = self.database_service.get_connection_settings()
        if connection_settings:
            self.set_ui_from_connection_settings(connection_settings)
        else:
            self.set_default_ui()

        self.set_authentication_radio(self.schema_connection_details.auth_type)
        self.update_mongo_uri()
        self.setup_connections()

    def set_ui_from_connection_settings(self, connection_settings):
        """Populate UI from connection settings."""
        self.form_ui.text_Host.setPlainText(connection_settings['host'])
        self.form_ui.text_Port.setPlainText(str(connection_settings['port']))
        self.form_ui.text_Username.setPlainText(connection_settings['user'])
        self.form_ui.text_Password.setPlainText(connection_settings['password'])
        self.form_ui.text_DbName.setPlainText(connection_settings['db_name'])
        self.form_ui.text_AuthSource.setPlainText(connection_settings['auth_source'])
        self.form_ui.text_SSH_Host.setPlainText(connection_settings['ssh_host'])
        self.form_ui.text_SSH_Port.setPlainText(str(connection_settings['ssh_port']))
        self.form_ui.text_SSH_Username.setPlainText(connection_settings['ssh_username'])
        self.form_ui.text_SSH_Password.setPlainText(connection_settings['ssh_password'])

    def set_default_ui(self):
        """Set default UI values."""
        self.form_ui.text_Host.setPlainText("localhost")
        self.form_ui.text_Port.setPlainText("27017")
        self.form_ui.text_Username.setPlainText("")
        self.form_ui.text_Password.setPlainText("")
        self.form_ui.text_DbName.setPlainText("test_db")
        self.form_ui.text_AuthSource.setPlainText("admin")

    def set_authentication_radio(self, auth_type):
        """Set the appropriate radio button for authentication type."""
        auth_map = {
            "MONGODB-X509": self.form_ui.radio_X509,
            "SCRAM-SHA-1": self.form_ui.radio_SHA1,
            "MONGODB-AWS": self.form_ui.radio_AWS,
            "PLAIN": self.form_ui.radio_KERBEROS_2,
            "SCRAM-SHA-256": self.form_ui.radio_SHA256,
            "GSSAPI (Kerberos)": self.form_ui.radio_KERBEROS,
            "LDAP": self.form_ui.radio_LDAP
        }

        for radio_button in auth_map.values():
            radio_button.setChecked(False)

        if auth_type and auth_type in auth_map:
            auth_map[auth_type].setChecked(True)

    def update_mongo_uri(self):
        """Generate Mongo URI based on user input."""
        uri = self.build_mongo_uri()
        self.form_ui.text_MongoUri.setPlainText(uri)

    def build_mongo_uri(self):
        """Build Mongo URI from the connection details stored in schema."""
        connection_details = self.schema_connection_details
        uri = f"mongodb://{connection_details.user}:{connection_details.password}@" \
              f"{connection_details.host}:{connection_details.port}/" \
              f"{connection_details.db_name}?authSource={connection_details.auth_source}"
        if connection_details.auth_type:
            uri += f"&authMechanism={connection_details.auth_type}"
        return uri

    def setup_connections(self):
        """Setup signal-slot connections."""
        self.form_ui.checkbox_SSH.toggled.connect(self.toggle_ssh_options)
        self.form_ui.setup_text_changed_connections()
        self.form_ui.setup_radio_button_connections()

    def toggle_ssh_options(self, is_checked):
        """Toggle visibility of SSH options based on checkbox."""
        ssh_elements = [
            self.form_ui.text_SSH_Host, self.form_ui.text_SSH_Port, self.form_ui.text_SSH_Username,
            self.form_ui.text_SSH_Password, self.form_ui.label_ssh_host, self.form_ui.label_ssh_port,
            self.form_ui.label_ssh_username, self.form_ui.label_ssh_password
        ]
        for element in ssh_elements:
            element.setVisible(is_checked)
