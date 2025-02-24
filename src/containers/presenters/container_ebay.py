from dependency_injector import containers, providers
from src.view.presenters.form_ebay.presenter_ebay import EbayWindowPresenter

class EbayPresentersContainer(containers.DeclarativeContainer):
    """Container for eBay-related presenters."""

    # Dependencies
    controllers = providers.DependenciesContainer()
    services = providers.DependenciesContainer()

    # Main eBay presenter factory
    ebay_presenter = providers.Factory(
        EbayWindowPresenter,
        ebay_controller=controllers.ebay_controller,
        notification_service=services.service_notification
    )