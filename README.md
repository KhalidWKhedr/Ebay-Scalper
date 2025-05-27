# Ebay-Scalper

A modular, well-structured Python application for automating eBay data collection, database management, and notification workflows. The codebase demonstrates clear separation of concerns, maintainable practices, and a professional approach to scalable Python backend projects.

---

## Project Highlights

- **Layered, Modular Design:**  
  Implements controllers, services, and models for a clean separation of workflow, business logic, and data handling.
- **Extensible Architecture:**  
  Each component (e.g., CSV export, database, eBay integration, notification) is isolated in its own module, making it easy to extend or maintain.
- **Robust Foundation:**  
  Uses dependency injection principles and a “container” approach to wire up and run the application.
- **Consistent Naming:**  
  Every file and directory is named for its role, aiding discoverability and comprehension.
- **Professional Quality:**  
  The code follows Python best practices and demonstrates sound understanding of scalable project organization.

---

## Project Structure

```
main.py           # Application entry point (wires containers, runs main loop)
requirements.txt  # Python dependencies
/src/             # Core application code
  ├─ config/                # Configuration and settings
  ├─ containers/            # Dependency injection/application wiring
  ├─ controllers/           # Request/workflow orchestration
      ├─ controller_csv.py
      ├─ controller_database.py
      ├─ controller_ebay.py
      ├─ controller_main.py
      └─ __init__.py
  ├─ services/              # Business logic and integrations
      ├─ service_csv.py
      ├─ service_database.py
      ├─ service_ebay.py
      ├─ service_notification.py
      └─ __init__.py
  ├─ models/                # Data models and schemas
      ├─ model_database_connection_details.py
      ├─ model_site_domain_ebay.py
      └─ __init__.py
  ├─ infrastructure/        # System-level or external service integration
  ├─ logger/                # Logging utilities
  ├─ utils/                 # Helper functions/utilities
  └─ view/                  # Presentation/output formatting
/query_csv/      # Data exports (CSV files)
/deprecated/     # Legacy or unused code
```

---

## Code Quality & Practices

- **Code Structure:**  
  - Controllers coordinate between services and models.
  - Services encapsulate business logic and external system interactions.
  - Models represent data and configuration.
- **Maintainability:**  
  - New features can be added by introducing new modules/services with minimal side effects.
  - Each controller/service/model is small and focused on a single responsibility.
- **Readability:**  
  - Code is commented and organized for clarity.
  - Naming is descriptive and consistent.
- **Extensibility:**  
  - The container approach enables easy swapping or extension of dependencies.

---

## Requirements

- Python 3.10+
- See `requirements.txt` for all dependencies:
  - cryptography
  - dependency_injector
  - ebaysdk
  - pandas
  - paramiko
  - pydantic
  - pymongo
  - PyMySQL
  - PySide6
  - python-dotenv
  - sshtunnel

_Install with:_
```sh
pip install -r requirements.txt
```

---

## Running the Application

```sh
python main.py
```
> The application initializes its dependency container, configures main window/presentation, and starts an event loop.

---

## Extending & Customizing

- **Add a new eBay workflow:** Create a new controller/service pair and wire it in via the container.
- **Support a new data model:** Add a model in `/src/models` and update related services/controllers.
- **Change storage or notification logic:** Update or extend the relevant service.

---

## Areas for Improvement

- Add end-to-end documentation and usage examples.
- Provide environment variable/configuration instructions.
- Add automated tests and CI/CD.
- Specify a license.
- Remove IDE-specific files from version control.

---

## License

_No license specified._

---

## Further Exploration

- Review the [src/controllers](https://github.com/KhalidWKhedr/Ebay-Scalper/tree/master/src/controllers) and [src/services](https://github.com/KhalidWKhedr/Ebay-Scalper/tree/master/src/services) folders for workflow and logic details.
- Explore `main.py` for application wiring and startup.

---
