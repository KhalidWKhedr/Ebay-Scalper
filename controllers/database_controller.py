from PySide6.QtWidgets import QDialog
from database.DatabaseService import DatabaseService
from services.NotificationService import NotificationService
from ui.gui_form_database import Ui_form_Database
from logger.LoggingService import LoggingService


class DatabaseController(QDialog, Ui_form_Database):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_service = DatabaseService()
        self.notification_service = NotificationService()
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
            'host': self.text_Host.toPlainText(),
            'port': int(self.text_Port.toPlainText()),
            'user': self.text_Username.toPlainText(),
            'password': self.text_Password.toPlainText(),
            'db_name': self.text_DbName.toPlainText(),
            'auth_source': self.text_AuthSource.toPlainText(),
            'ssh_host': self.text_SSH_Host.toPlainText(),
            'ssh_port': int(self.text_SSH_Port.toPlainText()),
            'ssh_username': self.text_SSH_Username.toPlainText(),
            'ssh_password': self.text_SSH_Password.toPlainText(),
        }
