from src.view.gui.gui_form_database import Ui_form_Database
from utils.utils_auth import get_selected_auth_type


class AuthenticationPresenter:
    def __init__(
        self,
        ui: Ui_form_Database
    ):
        self.ui = ui

    def set_authentication_radio(self, auth_type: str) -> None:
        """Set the appropriate radio button for authentication type."""
        auth_map = {
            "MONGODB-X509": self.ui.radio_X509,
            "SCRAM-SHA-1": self.ui.radio_SHA1,
            "MONGODB-AWS": self.ui.radio_AWS,
            "PLAIN": self.ui.radio_KERBEROS_2,
            "SCRAM-SHA-256": self.ui.radio_SHA256,
            "GSSAPI (Kerberos)": self.ui.radio_KERBEROS,
            "LDAP": self.ui.radio_LDAP
        }

        for radio_button in auth_map.values():
            radio_button.setChecked(False)

        if auth_type and auth_type in auth_map:
            auth_map[auth_type].setChecked(True)

    def get_selected_auth_type(self) -> str | None:
        return get_selected_auth_type(self.ui)
