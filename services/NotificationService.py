from PySide6.QtWidgets import QMessageBox
from logger.LoggingService import LoggingService


class NotificationService:
    def __init__(self):
        self.logger = LoggingService.get_logger()

    def show_message(self, parent, message):
        """Handles logging and displaying messages to the user."""

        self.logger.info(f"Notification: {message}")

        if "Error" in message:
            self.logger.error(f"Error: {message}")
            QMessageBox.critical(parent, "Connection Error", message)
        else:
            self.logger.info(f"Info: {message}")
            QMessageBox.information(parent, "Connection Successful", message)
