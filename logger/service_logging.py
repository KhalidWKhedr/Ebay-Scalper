import logging


class LoggingService:
    @staticmethod
    def get_logger():
        """Returns a logger instance for MongoConnectionLogger."""
        logger = logging.getLogger("MongoConnectionLogger")

        if not logger.hasHandlers():
            logger.setLevel(logging.DEBUG)
            ch = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            logger.addHandler(ch)

        return logger

    @staticmethod
    def log(message, level="INFO"):
        """Log a message with the given severity level."""
        level = level.lower()
        valid_levels = ["debug", "info", "warning", "error", "exception", "critical"]

        if level not in valid_levels:
            level = "info"  # Default to info if invalid level provided
            message = f"Invalid log level specified. Defaulting to INFO: {message}"

        logger = LoggingService.get_logger()
        log_method = getattr(logger, level, logger.info)  # Default to info if level is invalid
        log_method(message)


# Example Usage:
LoggingService.log("This is an info message")  # Logs as INFO by default
LoggingService.log("This is an error message", level="ERROR")  # Logs as ERROR
LoggingService.log("This is a success message", level="INFO")  # Logs as INFO
LoggingService.log("This is a message with an invalid level", level="INVALID")  # Logs as INFO with default message
