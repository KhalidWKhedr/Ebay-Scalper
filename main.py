from src.containers.container_application import ApplicationContainer

# Initialize DI container
container = ApplicationContainer()

# Initialize Qt application
app = container.app()

# Create the main window presenter
main_window = container.core.ui.main_presenter()

# Show the main window
main_window.show()

# Start the application event loop
app.exec()