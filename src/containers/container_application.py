from dependency_injector import containers, providers
from PySide6.QtWidgets import QApplication
import sys
from .container_core import CoreContainer

class ApplicationContainer(containers.DeclarativeContainer):
    """Application container for managing the Qt application."""
    core = providers.Container(CoreContainer)
    app = providers.Singleton(QApplication, sys.argv) 