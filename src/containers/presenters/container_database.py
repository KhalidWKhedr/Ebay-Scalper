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
    auth_presenter_factory = providers.Factory(
        AuthenticationPresenter,
        database_controller=controllers.database_controller,
        notification_service=services.notification_service
    )

    connection_settings_presenter_factory = providers.Factory(
        ConnectionSettingsPresenter,
        database_controller=controllers.database_controller,
        notification_service=services.notification_service
    )

    mongo_uri_presenter_factory = providers.Factory(
        MongoURIPresenter,
        database_controller=controllers.database_controller,
        notification_service=services.notification_service
    )

    ssh_presenter_factory = providers.Factory(
        SSHPresenter,
        database_controller=controllers.database_controller,
        notification_service=services.notification_service
    )

    # Main database presenter factory
    database_presenter = providers.Singleton(
        DatabaseWindowPresenter,
        database_controller=controllers.database_controller,
        notification_service=services.notification_service,
        auth_presenter=auth_presenter_factory,
        connection_settings_presenter=connection_settings_presenter_factory,
        mongo_uri_presenter=mongo_uri_presenter_factory,
        ssh_presenter=ssh_presenter_factory
    )