from dependency_injector import containers, providers
from src.view.presenters.form_main.presenter_main import MainPresenter
from src.view.gui.gui_form_main import Ui_form_MainWindow
from src.view.presenters.form_main.presenter_csv import CsvPresenter
from ..container_controllers import ControllersContainer
from ..container_services import ServicesContainer
from ...view.gui.gui_form_database import Ui_form_Database
from ...view.presenters.form_main.presenter_query import QueryPresenter


class MainPresentersContainer(containers.DeclarativeContainer):
    """Container for managing presenter-related dependencies."""
    controllers = providers.Container(ControllersContainer)
    services = providers.Container(ServicesContainer)

    # UI components
    main_ui = providers.Singleton(Ui_form_MainWindow)
    database_ui = providers.Singleton(Ui_form_Database)

    # Presenters
    csv_presenter = providers.Singleton(
        CsvPresenter,
        csv_controller=controllers.csv_controller,
        notification_service=services.service_notification
    )

    query_presenter = providers.Singleton(
        QueryPresenter,
        ebay_controller=controllers.ebay_controller,
        notification_service=services.service_notification
    )

    main_presenter = providers.Singleton(
        MainPresenter,
        main_ui=main_ui,
        main_controller=controllers.main_controller,
        csv_controller=controllers.csv_controller,
        notification_service=services.service_notification,
        csv_presenter=csv_presenter,
        query_presenter=query_presenter
    )
