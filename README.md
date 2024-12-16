eBay_Scalp

Overview:
eBay_Scalp is a Python-based application that integrates with the eBay API to scrape data based on user-provided queries. These queries are read from a CSV file, and the results are stored securely in a MongoDB database. The project uses advanced features like SSH tunneling for secure database connections, modular architecture, and a flexible MongoDB integration.

Key Features:

    eBay API Integration
        Uses the ebaysdk library to perform advanced item searches on eBay.
        Dynamically processes and handles large datasets from a user-provided Excel or CSV file.

    Data Handling and Storage
        Extracts structured data (e.g., item information, pricing, shipping details) from eBay's responses using a modular EbayJsonExtractor.
        Stores data in a MongoDB database, categorized by query strings.
        Includes reusable MongoDB operations for data insertion and retrieval.

    Secure SSH Connection
        Uses SSHTunnelForwarder to securely connect to a remote MongoDB server.
        Environment variables manage sensitive credentials securely.

    User-Friendly Interface (In Progress)
        A graphical user interface (GUI) is under development to enhance usability for non-technical users.

    Modular Design
        Separation of concerns through distinct modules for database connection, data extraction, and eBay API communication.

Technologies Used:

    Python Libraries: Pandas, eBay SDK, PyMongo, SSHTunnel
    Database: MongoDB
    Environment Management: Dotenv for secure handling of API keys and credentials
