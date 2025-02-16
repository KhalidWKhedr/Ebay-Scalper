from dependency_injector import containers, providers
from src.utils.utils_manager_secure_config import SecureConfigManager
from src.utils.utils_converter import Converter


class UtilsContainer(containers.DeclarativeContainer):
    """Container for utility classes."""

    secure_config_manager = providers.Singleton(SecureConfigManager)
    converter = providers.Singleton(Converter)