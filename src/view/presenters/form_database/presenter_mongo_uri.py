from src.models.model_database_connection_details import SchemaConnectionDetails
from src.utils.utils_auth import get_selected_auth_type


class MongoURIPresenter:
    """Handles MongoDB URI generation and updates."""

    def __init__(
        self,
        host_field, port_field, username_field, password_field,
        db_name_field, auth_source_field, mongo_uri_field,
        ssh_host_field, ssh_port_field, ssh_username_field, ssh_password_field,
        auth_radio_buttons
    ):
        self.host_field = host_field
        self.port_field = port_field
        self.username_field = username_field
        self.password_field = password_field
        self.db_name_field = db_name_field
        self.auth_source_field = auth_source_field
        self.mongo_uri_field = mongo_uri_field
        self.ssh_host_field = ssh_host_field
        self.ssh_port_field = ssh_port_field
        self.ssh_username_field = ssh_username_field
        self.ssh_password_field = ssh_password_field
        self.auth_radio_buttons = auth_radio_buttons

    def update_mongo_uri(self) -> None:
        """Update the MongoDB URI in the UI."""
        uri = self.build_mongo_uri()
        self.mongo_uri_field.setPlainText(uri)

    def build_mongo_uri(self) -> str:
        """Generate the MongoDB URI based on user input."""
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
            SSH_TOGGLE=self.ssh_host_field.isVisible(),
            MONGO_HOST=self.host_field.toPlainText().strip(),
            MONGO_PORT=self.port_field.toPlainText().strip(),
            MONGO_USER=self.username_field.toPlainText().strip(),
            MONGO_PASSWORD=self.password_field.toPlainText().strip(),
            MONGO_DB_NAME=self.db_name_field.toPlainText().strip(),
            MONGO_AUTH_DB=self.auth_source_field.toPlainText().strip(),
            SSH_HOST=self.ssh_host_field.toPlainText().strip(),
            SSH_PORT=self.ssh_port_field.toPlainText().strip(),
            SSH_USERNAME=self.ssh_username_field.toPlainText().strip(),
            SSH_PASSWORD=self.ssh_password_field.toPlainText().strip(),
            AUTH_TYPE=self.get_selected_auth_type(),
        )

    def get_selected_auth_type(self) -> str | None:
        """Get the selected authentication type from the UI."""
        return get_selected_auth_type(self.auth_radio_buttons)