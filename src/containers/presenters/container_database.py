from dependency_injector import containers, providers
from src.view.presenters.form_database import (
    DatabaseWindowPresenter,
    AuthenticationPresenter,
    ConnectionSettingsPresenter,
    MongoURIPresenter,
    SSHPresenter
)

class DatabasePresentersContainer(containers.DeclarativeContainer):
    """Container for database-related presenters."""

    # Dependencies
    controllers = providers.DependenciesContainer()
    services = providers.DependenciesContainer()

    # Factories for lazy instantiation
    auth_presenter = providers.Factory(
        AuthenticationPresenter,
        database_controller=controllers.database_controller,
        notification_service=services.service_notification
    )

    connection_settings_presenter = providers.Factory(
        ConnectionSettingsPresenter,
        database_controller=controllers.database_controller,
        notification_service=services.service_notification
    )

    mongo_uri_presenter = providers.Factory(
        MongoURIPresenter,
        database_controller=controllers.database_controller,
        notification_service=services.service_notification
    )

    ssh_presenter = providers.Factory(
        SSHPresenter,
        database_controller=controllers.database_controller,
        notification_service=services.service_notification
    )

    # Main database presenter factory
    database_presenter = providers.Factory(
        DatabaseWindowPresenter,
        database_controller=controllers.database_controller,
        notification_service=services.service_notification,
        auth_presenter=auth_presenter,
        connection_settings_presenter=connection_settings_presenter,
        mongo_uri_presenter=mongo_uri_presenter,
        ssh_presenter=ssh_presenter
    )