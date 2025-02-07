import sys
from PySide6.QtWidgets import QApplication

# --- Utils ---
from utils.converter import Converter
from utils.manager_secure_config import SecureConfigManager

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
from src.ui.presenter_main import MainPresenter


def initialize_services():
    """Initialize and return all required services."""
    # --- Initialize Utils ---
    logger = LoggingService()
    secure_config_manager = SecureConfigManager()
    utils_converter = Converter()

    # --- Initialize Services ---
    service_csv = CsvService(logger=logger)
    service_notification = NotificationService(logger=logger)
    service_ebay = EbayService(logger=logger, secure_config=secure_config_manager)

    mongo_manager = MongoConnectionManager(logger=logger, secure_config_manager=secure_config_manager)
    database_service = DatabaseService(logger=logger, secure_config=secure_config_manager, mongo_manager=mongo_manager)

    # --- Initialize Controllers ---
    csv_controller = CsvController(logger=logger, csv_service=service_csv)
    database_controller = DatabaseController(logger=logger, database_service=database_service, converter=utils_converter)
    ebay_controller = EbayApiController(logger=logger, ebay_service=service_ebay, site_domain_model=SiteDomainModel(site_domain_mapping=SITE_DOMAIN_MAPPING))
    main_controller = MainController(logger=logger, csv_controller=csv_controller, database_controller=database_controller, ebay_controller=ebay_controller, notification_service=service_notification)

    # Return all services and controllers in a dictionary
    return {
        'service_logging': logger,
        'csv_controller': csv_controller,
        'database_controller': database_controller,
        'ebay_controller': ebay_controller,
        'main_controller': main_controller,
        'service_notification': service_notification
    }


def main():
    """Main entry point for the application."""
    # --- Initialize Services ---
    services = initialize_services()

    # Create the Qt application
    app = QApplication(sys.argv)

    # Initialize the main application presenter with the services
    main_presenter = MainPresenter(
        main_controller=services['main_controller'],
        csv_controller=services['csv_controller'],
        notification_service=services['service_notification']
    )

    # Show the main window
    main_presenter.show()

    # Execute the application
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
