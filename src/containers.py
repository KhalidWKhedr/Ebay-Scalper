from dependency_injector import containers, providers
from PySide6.QtWidgets import QApplication

# --- Utils ---
from utils.utils_converter import Converter
from utils.utils_manager_secure_config import SecureConfigManager

# --- Services ---
from logger.service_logging import LoggingService
from src.services.service_database import DatabaseService
from src.services.service_csv import CsvService
from src.services.service_ebay import EbayService
from src.services.service_notification import NotificationService
from src.database.manager_mongo_connector import MongoConnectionManager
from src.ebay.manager_ebay_connection import EbayConnectionManager


# --- Controllers ---
from src.controllers.controller_csv import CsvController
from src.controllers.controller_database import DatabaseController
from src.controllers.controller_ebay_api import EbayApiController
from src.controllers.controller_main import MainController

# --- Models ---
from src.models.model_site_domain_ebay import SiteDomainModel
from src.config.site_domain_mapping_ebay import SITE_DOMAIN_MAPPING

# --- UI ---
from src.view.presenters.form_main.presenter_main import MainPresenter


class UtilsContainer(containers.DeclarativeContainer):
    """Container for utility classes."""

    secure_config_manager = providers.Singleton(
        SecureConfigManager)

    utils_converter = providers.Singleton(
        Converter)


class ServicesContainer(containers.DeclarativeContainer):
    """Container for service classes."""

    service_logging = providers.Singleton(
        LoggingService)

    service_csv = providers.Singleton(
        CsvService,
        logger=service_logging)

    service_notification = providers.Singleton(
        NotificationService,
        logger=service_logging)

    # Ebay API
    ebay_manager = providers.Singleton(
        EbayConnectionManager,
        logger=service_logging)

    service_ebay = providers.Singleton(
        EbayService,
        logger=service_logging,
        secure_config=UtilsContainer.secure_config_manager,
        ebay_connection_manager=ebay_manager)

    # MongoDB
    mongo_manager = providers.Singleton(
        MongoConnectionManager,
        logger=service_logging,
        secure_config_manager=UtilsContainer.secure_config_manager)

    database_service = providers.Singleton(
        DatabaseService,
        logger=service_logging,
        secure_config=UtilsContainer.secure_config_manager,
        mongo_manager=mongo_manager)


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


class UIContainer(containers.DeclarativeContainer):
    """Container for UI-related classes."""

    main_presenter = providers.Singleton(
        MainPresenter,
        main_controller=ControllersContainer.main_controller,
        csv_controller=ControllersContainer.csv_controller,
        notification_service=ServicesContainer.service_notification)


class CoreContainer(containers.DeclarativeContainer):
    """Core container for managing non-UI dependencies."""

    utils = providers.Container(UtilsContainer)
    services = providers.Container(ServicesContainer)
    controllers = providers.Container(ControllersContainer)
    ui = providers.Container(UIContainer)


class ApplicationContainer(containers.DeclarativeContainer):
    """Application container for managing the Qt application."""

    core = providers.Container(CoreContainer)
    app = providers.Singleton(QApplication)  # Keep it only if necessary