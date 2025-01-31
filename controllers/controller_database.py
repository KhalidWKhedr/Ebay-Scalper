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
        self.checkbox_SSH.toggled.connect(self.toggle_ssh_options)
        self.toggle_ssh_options(self.checkbox_SSH.isChecked())
        self.button_Connect.clicked.connect(self.connect_to_db)

    def connect_to_db(self):
        connection_details = self.get_connection_details()
        LoggingService.log(f"Attempting to connect to database at host: {connection_details['host']}", level="info")

        try:
            message = self.db_service.connect(connection_details)
            LoggingService.log(f"Connection to database successful: {message}", level="info")
        except Exception as e:
            LoggingService.log(f"Failed to connect to database: {str(e)}", level="error")

        self.notification_service.show_message(self, message)

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
        }

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
        self.text_Host.setVisible(False if is_checked else True)