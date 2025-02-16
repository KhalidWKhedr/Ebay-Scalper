from dependency_injector import containers, providers
from src.services import (
    DatabaseService,
    CsvService,
    EbayService,
    NotificationService
)
from .container_utils import UtilsContainer
from .container_logger import LoggerContainer
from .container_infrastructure import InfrastructureContainer


class ServicesContainer(containers.DeclarativeContainer):
    """Container for service classes."""

    # Include containers
    utils = providers.Container(UtilsContainer)
    logger = providers.Container(LoggerContainer)
    infrastructure = providers.Container(InfrastructureContainer)

    # Service providers
    service_csv = providers.Singleton(
        CsvService,
        logger=logger.logging_service
    )

    service_notification = providers.Singleton(
        NotificationService,
        logger=logger.logging_service
    )

    service_ebay = providers.Singleton(
        EbayService,
        logger=logger.logging_service,
        secure_config=utils.secure_config_manager,
        connector_ebay=infrastructure.connector_ebay
    )

    service_database = providers.Singleton(
        DatabaseService,
        logger=logger.logging_service,
        secure_config=utils.secure_config_manager,
        connector_mongo=infrastructure.connector_mongo
    )