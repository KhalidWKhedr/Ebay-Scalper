import sys
from PySide6.QtWidgets import QApplication
from src.controllers.controller_main import MainController
from src.database.manager_mongo_connector import MongoConnectionManager
from src.services.service_database import DatabaseService
from logger.service_logging import LoggingService
from src.models.model_database_connection_details import SchemaConnectionDetails
from src.services.service_ebay import EbayService
from src.services.service_notification import NotificationService
from utils.converter import Converter
from src.services.service_csv import CsvService
from utils.manager_secure_config import SecureConfigManager

def create_services():
    logger = LoggingService()
    secure_config_manager = SecureConfigManager()
    mongo_manager = MongoConnectionManager(secure_config_manager=secure_config_manager)

    database_service = DatabaseService(
        logger=logger,
        secure_config=secure_config_manager,
        mongo_manager=mongo_manager
    )

    utils_converter = Converter()
    service_notification = NotificationService()
    service_ebay = EbayService()
    service_csv = CsvService()

    schema_connection_details = SchemaConnectionDetails()

    return {
        'database_service': database_service,
        'logger': logger,
        'utils_converter': utils_converter,
        'service_notification': service_notification,
        'service_ebay': service_ebay,
        'service_csv': service_csv,
        'schema_connection_details': schema_connection_details
    }

def main():

    services = create_services()

    app = QApplication(sys.argv)
    window = MainController(
        db_service=services['database_service'],
        logger=services['logger'],
        converter=services['utils_converter'],
        notification_service=services['service_notification'],
        ebay_service=services['service_ebay'],
        csv_service=services['service_csv'],
        schema_connection_details=services['schema_connection_details']
    )

    window.show()  #
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
