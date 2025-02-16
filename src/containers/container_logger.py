from dependency_injector import containers, providers
from src.logger.service_logging import LoggingService


class LoggerContainer(containers.DeclarativeContainer):
    """Container for logging services."""

    logging_service = providers.Singleton(LoggingService)