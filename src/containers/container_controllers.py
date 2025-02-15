from dependency_injector import containers, providers
from src.controllers.controller_csv import CsvController
from src.controllers.controller_database import DatabaseController
from src.controllers.controller_ebay_api import EbayApiController
from src.controllers.controller_main import MainController
from src.models.model_site_domain_ebay import SiteDomainModel
from src.config.site_domain_mapping_ebay import SITE_DOMAIN_MAPPING
from .container_services import ServicesContainer
from .container_utils import UtilsContainer

class ControllersContainer(containers.DeclarativeContainer):
    """Container for controller classes."""
    csv_controller = providers.Singleton(
        CsvController,
        logger=ServicesContainer.service_logging,
        csv_service=ServicesContainer.service_csv)

    database_controller = providers.Singleton(
        DatabaseController,
        logger=ServicesContainer.service_logging,
        database_service=ServicesContainer.database_service,
        converter=UtilsContainer.utils_converter)

    ebay_controller = providers.Singleton(
        EbayApiController,
        logger=ServicesContainer.service_logging,
        ebay_service=ServicesContainer.service_ebay,
        site_domain_model=SiteDomainModel(site_domain_mapping=SITE_DOMAIN_MAPPING))

    main_controller = providers.Singleton(
        MainController,
        logger=ServicesContainer.service_logging,
        csv_controller=csv_controller,
        database_controller=database_controller,
        ebay_controller=ebay_controller,
        notification_service=ServicesContainer.service_notification) 