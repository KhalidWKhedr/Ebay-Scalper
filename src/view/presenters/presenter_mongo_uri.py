from src.models.model_database_connection_details import SchemaConnectionDetails
from src.view.gui.gui_form_database import Ui_form_Database


class MongoURIPresenter:
    def __init__(
        self, ui: Ui_form_Database,
        schema_connection_details: SchemaConnectionDetails
    ):
        self.ui = ui
        self.schema_connection_details = schema_connection_details

    def update_mongo_uri(self) -> None:
        """Generate Mongo URI based on user input."""
        uri = self.build_mongo_uri()
        self.ui.text_MongoUri.setPlainText(uri)

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
            SSH_TOGGLE=self.ui.checkbox_SSH.isChecked(),
            MONGO_HOST=self.ui.text_Host.toPlainText().strip(),
            MONGO_PORT=self.ui.text_Port.toPlainText().strip(),
            MONGO_USER=self.ui.text_Username.toPlainText().strip(),
            MONGO_PASSWORD=self.ui.text_Password.toPlainText().strip(),
            MONGO_DB_NAME=self.ui.text_DbName.toPlainText().strip(),
            MONGO_AUTH_DB=self.ui.text_AuthSource.toPlainText().strip(),
            SSH_HOST=self.ui.text_SSH_Host.toPlainText().strip(),
            SSH_PORT=self.ui.text_SSH_Port.toPlainText().strip(),
            SSH_USERNAME=self.ui.text_SSH_Username.toPlainText().strip(),
            SSH_PASSWORD=self.ui.text_SSH_Password.toPlainText().strip(),
            AUTH_TYPE=self.get_selected_auth_type(),
        )

    def get_selected_auth_type(self) -> str | None:
        """Get the selected authentication type from radio buttons."""
        auth_map = {
            self.ui.radio_X509: "MONGODB-X509",
            self.ui.radio_SHA1: "SCRAM-SHA-1",
            self.ui.radio_AWS: "MONGODB-AWS",
            self.ui.radio_KERBEROS_2: "PLAIN",
            self.ui.radio_SHA256: "SCRAM-SHA-256",
            self.ui.radio_KERBEROS: "GSSAPI (Kerberos)",
            self.ui.radio_LDAP: "LDAP"
        }

        for radio_button, auth_value in auth_map.items():
            if radio_button.isChecked():
                return auth_value
        return None