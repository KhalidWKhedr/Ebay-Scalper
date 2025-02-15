from dependency_injector import containers, providers
from src.logger.service_logging import LoggingService
from src.services.service_database import DatabaseService
from src.services.service_csv import CsvService
from src.services.service_ebay import EbayService
from src.services.service_notification import NotificationService
from src.database.manager_mongo_connector import MongoConnectionManager
from src.ebay.manager_ebay_connection import EbayConnectionManager
from .container_utils import UtilsContainer

class ServicesContainer(containers.DeclarativeContainer):
    """Container for service classes."""
    service_logging = providers.Singleton(LoggingService)
    
    service_csv = providers.Singleton(
        CsvService,
        logger=service_logging)

    service_notification = providers.Singleton(
        NotificationService,
        logger=service_logging)

    ebay_manager = providers.Singleton(
        EbayConnectionManager,
        logger=service_logging)

    service_ebay = providers.Singleton(
        EbayService,
        logger=service_logging,
        secure_config=UtilsContainer.secure_config_manager,
        ebay_connection_manager=ebay_manager)

    mongo_manager = providers.Singleton(
        MongoConnectionManager,
        logger=service_logging,
        secure_config_manager=UtilsContainer.secure_config_manager)

    database_service = providers.Singleton(
        DatabaseService,
        logger=service_logging,
        secure_config=UtilsContainer.secure_config_manager,
        mongo_manager=mongo_manager) 