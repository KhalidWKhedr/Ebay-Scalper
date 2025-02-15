from dependency_injector import containers, providers
from src.utils.utils_converter import Converter
from src.utils.utils_manager_secure_config import SecureConfigManager

class UtilsContainer(containers.DeclarativeContainer):
    """Container for utility classes."""
    secure_config_manager = providers.Singleton(SecureConfigManager)
    utils_converter = providers.Singleton(Converter)
