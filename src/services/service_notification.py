from PySide6.QtWidgets import QMessageBox
from logger.service_logging import LoggingService
from typing import Optional


class NotificationService:
    def __init__(self, logger: LoggingService):
        """Initialize with a logger instance."""
        self.logger = logger

    def show_message(self, parent, message: str, title: str = "Notification", level: str = "info"):
        """Handles logging and displaying messages to the user."""
        if level == "error":
            self.logger.get_logger().error(f"Error: {message}")
            QMessageBox.critical(parent, title, message)
        else:
            self.logger.get_logger().info(f"Info: {message}")
            QMessageBox.information(parent, title, message)

    def notify(self, param: Optional[str] = None):
        """Placeholder for additional notifications (can be expanded later)."""
        if param:
            self.logger.get_logger().info(f"Notification: {param}")
        # This can be expanded to more complex logic in the future.
