from dependency_injector import containers, providers
from src.view.presenters.form_main.presenter_main import MainPresenter
from src.view.gui.gui_form_main import Ui_form_MainWindow
from src.view.presenters.form_main.presenter_csv import CsvPresenter
from .container_controllers import ControllersContainer
from .container_services import ServicesContainer


class UIContainer(containers.DeclarativeContainer):
    """Container for UI-related classes."""
    controllers = providers.Container(ControllersContainer)
    services = providers.Container(ServicesContainer)

    # UI components
    main_ui = providers.Singleton(Ui_form_MainWindow)

    # Presenters
    csv_presenter = providers.Singleton(
        CsvPresenter,
        csv_controller=controllers.csv_controller,
        notification_service=services.service_notification
    )

    main_presenter = providers.Singleton(
        MainPresenter,
        main_ui=main_ui,
        main_controller=controllers.main_controller,
        csv_controller=controllers.csv_controller,
        notification_service=services.service_notification,
        csv_presenter=csv_presenter  # Inject the CsvPresenter
    )