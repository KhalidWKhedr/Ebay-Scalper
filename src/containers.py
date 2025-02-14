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


class CoreContainer(containers.DeclarativeContainer):
    """Core container for managing non-UI dependencies."""

    # --- Utils ---
    secure_config_manager = providers.Singleton(
        SecureConfigManager)

    utils_converter = providers.Singleton(
        Converter)

    # --- Services ---
    service_logging = providers.Singleton(
        LoggingService)

    service_csv = providers.Singleton(
        CsvService,
        logger=service_logging)

    service_notification = providers.Singleton(
        NotificationService,
        logger=service_logging)

    service_ebay = providers.Singleton(
        EbayService,
        logger=service_logging,
        secure_config=secure_config_manager)

    # MongoDB
    mongo_manager = providers.Singleton(
        MongoConnectionManager,
        logger=service_logging,
        secure_config_manager=secure_config_manager)

    database_service = providers.Singleton(
        DatabaseService,
        logger=service_logging,
        secure_config=secure_config_manager,
        mongo_manager=mongo_manager)

    # --- Controllers ---
    csv_controller = providers.Singleton(
        CsvController,
        logger=service_logging,
        csv_service=service_csv)

    database_controller = providers.Singleton(
        DatabaseController,
        logger=service_logging,
        database_service=database_service,
        converter=utils_converter)

    ebay_controller = providers.Singleton(
        EbayApiController,
        logger=service_logging,
        ebay_service=service_ebay,
        site_domain_model=SiteDomainModel(site_domain_mapping=SITE_DOMAIN_MAPPING))

    main_controller = providers.Singleton(
        MainController,
        logger=service_logging,
        csv_controller=csv_controller,
        database_controller=database_controller,
        ebay_controller=ebay_controller,
        notification_service=service_notification)

    # --- UI ---
    main_presenter = providers.Singleton(
        MainPresenter,
        main_controller=main_controller,
        csv_controller=csv_controller,
        notification_service=service_notification)


class ApplicationContainer(containers.DeclarativeContainer):
    """Application container for managing the Qt application."""

    core = providers.Container(CoreContainer)

    app = providers.Singleton(QApplication)  # Keep it only if necessary
