from PySide6.QtWidgets import QDialog
from src.controllers.controller_database import DatabaseController
from src.view.gui.gui_form_database import Ui_form_Database
from src.view.presenters.form_database.presenter_authentication import AuthenticationPresenter
from src.view.presenters.form_database.presenter_connection_settings import ConnectionSettingsPresenter
from src.view.presenters.form_database.presenter_mongo_uri import MongoURIPresenter
from src.view.presenters.form_database.presenter_ssh import SSHPresenter


class DatabaseWindowPresenter(QDialog, Ui_form_Database):
    """Handles the database settings window and its interactions."""

    def __init__(self, notification_service, database_controller: DatabaseController):
        super().__init__()
        self.setupUi(self)

        self.notification_service = notification_service
        self.database_controller = database_controller
        self.schema_connection_details = self.database_controller.get_connection_settings()

        # Initialize Presenters
        self._init_presenters()

        # Setup UI and event connections
        self._setup_ui()

    def _init_presenters(self) -> None:
        """Initialize related presenters."""
        self.connection_settings_presenter = ConnectionSettingsPresenter(self)
        self.authentication_presenter = AuthenticationPresenter(self)
        self.mongo_uri_presenter = MongoURIPresenter(self)
        self.ssh_presenter = SSHPresenter(self)

    def _setup_ui(self) -> None:
        """Initialize UI components and set up connections."""
        self._load_connection_settings()
        self._setup_signal_connections()

    def _load_connection_settings(self) -> None:
        """Load stored connection settings into the UI."""
        self.connection_settings_presenter.load_connection_settings(self.schema_connection_details)
        self.authentication_presenter.set_authentication_radio(self.schema_connection_details.get("AUTH_TYPE", ""))
        self.mongo_uri_presenter.update_mongo_uri()

    def _setup_signal_connections(self) -> None:
        """Set up UI signal-slot connections."""
        self.checkbox_SSH.toggled.connect(self.ssh_presenter.toggle_ssh_options)
        self.button_Connect.clicked.connect(self.connect_to_db)
        self.button_SaveDetails.clicked.connect(self.save_connection_settings)

        self._connect_text_fields()
        self._connect_radio_buttons()

        # Ensure SSH options toggle correctly on startup
        self.ssh_presenter.toggle_ssh_options(self.checkbox_SSH.isChecked())

    def _connect_text_fields(self) -> None:
        """Connect text fields to update Mongo URI dynamically."""
        text_fields = [
            self.text_SSH_Host, self.text_SSH_Port, self.text_SSH_Username,
            self.text_SSH_Password, self.text_Host, self.text_Port,
            self.text_Username, self.text_Password, self.text_DbName,
            self.text_AuthSource
        ]
        for field in text_fields:
            field.textChanged.connect(self.mongo_uri_presenter.update_mongo_uri)

    def _connect_radio_buttons(self) -> None:
        """Connect radio buttons to dynamically update authentication type."""
        radio_buttons = [
            self.radio_X509, self.radio_SHA1, self.radio_AWS,
            self.radio_KERBEROS_2, self.radio_SHA256, self.radio_KERBEROS,
            self.radio_LDAP
        ]
        for button in radio_buttons:
            button.toggled.connect(self.mongo_uri_presenter.update_mongo_uri)

    # ========== Business Logic ==========

    def connect_to_db(self) -> None:
        """Attempt to connect to the database and display result."""
        try:
            connection_details = self.mongo_uri_presenter.get_connection_details()
            message = self.database_controller.connect_to_db(connection_details)
            self.notification_service.show_message(self, message)
        except Exception as e:
            self.notification_service.show_message(self, f"Error: {str(e)}")

    def save_connection_settings(self) -> None:
        """Save the current database connection settings."""
        try:
            connection_details = self.mongo_uri_presenter.get_connection_details()
            message = self.database_controller.save_connection_settings(connection_details)
            self.notification_service.show_message(self, message)
        except Exception as e:
            self.notification_service.show_message(self, f"Error: {str(e)}")
