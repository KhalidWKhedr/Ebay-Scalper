from src.containers import ApplicationContainer

# Initialize DI container
container = ApplicationContainer()

# Initialize Qt application
app = container.app()

# Create the main window presenter
main_window = container.core.main_presenter()

main_window.show()
app.exec()
