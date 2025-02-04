import logging
from logging.handlers import RotatingFileHandler
from typing import Optional


class LoggingService:
    _logger: Optional[logging.Logger] = None

    @staticmethod
    def _initialize_logger() -> logging.Logger:
        """Initialize and configure the logger."""
        logger = logging.getLogger("MongoConnectionLogger")
        logger.setLevel(logging.DEBUG)

        if not logger.hasHandlers():
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            logger.addHandler(ch)

            log_file = "app.log"
            fh = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=5)  # 10 MB per file, 5 backups
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        return logger

    @classmethod
    def get_logger(cls) -> logging.Logger:
        """Returns a singleton logger instance."""
        if cls._logger is None:
            cls._logger = cls._initialize_logger()
        return cls._logger

    @classmethod
    def log(cls, message: str, level: str = "INFO", **kwargs) -> None:
        """Log a message with the given severity level and optional context."""
        level = level.upper()
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

        if level not in valid_levels:
            level = "INFO"
            message = f"Invalid log level specified. Defaulting to INFO: {message}"

        logger = cls.get_logger()
        log_method = getattr(logger, level.lower(), logger.info)
        log_method(message, **kwargs)

    @classmethod
    def log_exception(cls, message: str, exc_info: Optional[Exception] = None) -> None:
        """Log an exception with traceback information."""
        logger = cls.get_logger()
        logger.error(message, exc_info=exc_info)

    @classmethod
    def set_log_level(cls, level: str) -> None:
        """Set the log level dynamically."""
        level = level.upper()
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

        if level not in valid_levels:
            raise ValueError(f"Invalid log level: {level}. Valid levels are {valid_levels}")

        logger = cls.get_logger()
        logger.setLevel(level)
        for handler in logger.handlers:
            handler.setLevel(level)

    @classmethod
    def add_file_handler(cls, log_file: str, max_bytes: int = 10 * 1024 * 1024, backup_count: int = 5) -> None:
        """Add a file handler with log rotation."""
        logger = cls.get_logger()
        fh = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    @classmethod
    def remove_all_handlers(cls) -> None:
        """Remove all handlers from the logger."""
        logger = cls.get_logger()
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

