from dependency_injector import containers, providers
from src.controllers import (
    CsvController,
    DatabaseController,
    EbayController,
    MainController
)
from src.models.model_site_domain_ebay import SiteDomainModel
from src.config.site_domain_mapping_ebay import SITE_DOMAIN_MAPPING
from .container_services import ServicesContainer
from .container_logger import LoggerContainer

class ControllersContainer(containers.DeclarativeContainer):
    """Container for controller classes."""
    services = providers.Container(ServicesContainer)
    logger = providers.Container(LoggerContainer)
    
    csv_controller = providers.Singleton(
        CsvController,
        logger=logger.logging_service,
        csv_service=services.service_csv
    )
    
    database_controller = providers.Singleton(
        DatabaseController,
        logger=logger.logging_service,
        database_service=services.service_database,
        converter=services.utils.converter
    )
    
    ebay_controller = providers.Singleton(
        EbayController,
        logger=logger.logging_service,
        ebay_service=services.service_ebay,
        site_domain_model=providers.Factory(
            SiteDomainModel,
            site_domain_mapping=SITE_DOMAIN_MAPPING
        )
    )
    
    main_controller = providers.Singleton(
        MainController,
        logger=logger.logging_service,
        csv_controller=csv_controller,
        database_controller=database_controller,
        ebay_controller=ebay_controller,
        notification_service=services.service_notification
    ) 