from PySide6.QtWidgets import QMessageBox, QWidget
from logger.service_logging import LoggingService
from typing import Optional


class NotificationService:
    def __init__(self, logger: LoggingService):
        """Initialize with a logger instance."""
        self.logger = logger

    def show_message(self, parent: QWidget, message: str, title: str = "Notification", level: str = "info"):
        """Handles logging and displaying messages to the user."""
        if level == "error":
            self.logger.get_logger().error(f"Error: {message}")
            QMessageBox.critical(parent, title, message)
        elif level == "warning":
            self.logger.get_logger().warning(f"Warning: {message}")
            QMessageBox.warning(parent, title, message)
        elif level == "critical":
            self.logger.get_logger().critical(f"Critical: {message}")
            QMessageBox.critical(parent, title, message)
        else:  # Default to info
            self.logger.get_logger().info(f"Info: {message}")
            QMessageBox.information(parent, title, message)

    def notify(self, param: Optional[str] = None):
        """Placeholder for additional notifications (can be expanded later)."""
        if param:
            self.logger.get_logger().info(f"Notification: {param}")
        # This can be expanded to more complex logic in the future.
