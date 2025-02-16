from dependency_injector import containers, providers
from src.infrastructure.external.connector_ebay import ConnectorEbay
from src.infrastructure.database.connector_mongo import ConnectorMongo
from .container_utils import UtilsContainer
from .container_logger import LoggerContainer

class InfrastructureContainer(containers.DeclarativeContainer):
    """Container for infrastructure dependencies."""
    
    # Include other containers
    utils = providers.Container(UtilsContainer)
    logger = providers.Container(LoggerContainer)
    
    # Infrastructure providers
    connector_ebay = providers.Factory(
        ConnectorEbay,
        logger=logger.logging_service
    )

    connector_mongo = providers.Factory(
        ConnectorMongo,
        logger=logger.logging_service,
        secure_config_manager=utils.secure_config_manager
    )

