from PySide6.QtWidgets import QMessageBox
from logger.service_logging import LoggingService


class NotificationService:
    def __init__(self, logger: LoggingService):
        self.logger = logger

    def show_message(self, parent, message, title="Notification", level="info"):
        """Handles logging and displaying messages to the user. """
        if level == "error":
            self.logger.error(f"Error: {message}")
            QMessageBox.critical(parent, title, message)
        else:
            self.logger.get_logger().info(f"Info: {message}")
            QMessageBox.information(parent, title, message)

    def notify(self, param):
        """Placeholder for additional notifications (can be expanded later)."""
        pass