from dependency_injector import containers, providers
from .container_utils import UtilsContainer
from .container_services import ServicesContainer
from .container_controllers import ControllersContainer
from .container_ui import UIContainer

class CoreContainer(containers.DeclarativeContainer):
    """Core container for managing application dependencies."""
    utils = providers.Container(UtilsContainer)
    services = providers.Container(ServicesContainer)
    controllers = providers.Container(ControllersContainer)
    ui = providers.Container(UIContainer) 