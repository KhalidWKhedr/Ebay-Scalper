from src.models.model_database_connection_details import SchemaConnectionDetails
from src.view.gui.gui_form_database import Ui_form_Database
from utils.utils_auth import get_selected_auth_type

class MongoURIPresenter:
    def __init__(
        self, ui: Ui_form_Database,
    ):
        self.ui = ui

    def update_mongo_uri(self) -> None:
        """Generate Mongo URI based on user input."""
        uri = self.build_mongo_uri()
        self.ui.text_MongoUri.setPlainText(uri)

    def build_mongo_uri(self) -> str:
        connection_details = self.get_connection_details()

        credentials = ""
        if connection_details.MONGO_USER and connection_details.MONGO_PASSWORD:
            credentials = f"{connection_details.MONGO_USER}:{connection_details.MONGO_PASSWORD}@"

        uri = f"mongodb://{credentials}{connection_details.MONGO_HOST}:{connection_details.MONGO_PORT}/" \
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
        return get_selected_auth_type(self.ui)
