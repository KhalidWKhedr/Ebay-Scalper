import sys

# from core import EbayItemFetcher
from PySide6.QtWidgets import QApplication
from sshtunnel import SSHTunnelForwarder

from controllers.controller_main import MainController
from deprecated.past_code.MongoSSHConnector import MongoSSHConnector


def create_tunnel():
    """Creates the SSH tunnel."""
    try:
        tunnel = SSHTunnelForwarder(
            ('192.168.120', 22),
            ssh_username='Khalid',
            ssh_password='Fuckrtu@1',
            remote_bind_address=('localhost', 27017),
            local_bind_address=("localhost", 27018)  # Local port for the SSH tunnel
        )
        tunnel.start()
        print("SSH tunnel established.")
    except Exception as e:
        print(f"Error establishing SSH tunnel: {e}")



if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application
    window = MainController()  # Create the window
    window.show()  # Show the window
    sys.exit(app.exec())  # Start the application event loop
    # EbayScrapper = EbayItemFetcher.EbayScraping()
    # EbayScrapper.check_app_id()
    # EbayScrapper.connect_to_ebay()
    # EbayScrapper.scrap_ebay()



