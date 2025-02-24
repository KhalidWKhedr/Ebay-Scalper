"""Presenters Container Package"""
from dependency_injector import containers, providers
from .container_database import DatabasePresentersContainer
from .container_main import MainPresentersContainer
from .container_ebay import EbayPresentersContainer

class PresentersContainer(containers.DeclarativeContainer):
    """Root container for all presenters."""
    
    # Dependencies
    controllers = providers.DependenciesContainer()
    services = providers.DependenciesContainer()

    # Sub-containers
    database = providers.Container(
        DatabasePresentersContainer,
        controllers=controllers,
        services=services
    )

    main = providers.Container(
        MainPresentersContainer,
        controllers=controllers,
        services=services
    )

    ebay = providers.Container(
        EbayPresentersContainer,
        controllers=controllers,
        services=services
    )

    # Expose main presenter for application container
    main_presenter = main.main_presenter

__all__ = ['PresentersContainer']
