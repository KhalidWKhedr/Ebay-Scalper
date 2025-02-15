from dependency_injector import containers, providers
from src.view.presenters.form_main.presenter_main import MainPresenter
from .container_controllers import ControllersContainer
from .container_services import ServicesContainer

class UIContainer(containers.DeclarativeContainer):
    """Container for UI-related classes."""
    main_presenter = providers.Singleton(
        MainPresenter,
        main_controller=ControllersContainer.main_controller,
        csv_controller=ControllersContainer.csv_controller,
        notification_service=ServicesContainer.service_notification) 