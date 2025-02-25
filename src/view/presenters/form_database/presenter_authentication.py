from src.utils.utils_auth import get_selected_auth_type


class AuthenticationPresenter:
    """Handles authentication-related UI interactions."""

    def __init__(self, auth_radio_buttons):
        self.auth_radio_buttons = auth_radio_buttons

    def set_authentication_radio(self, auth_type: str) -> None:
        """Set the appropriate radio button for authentication type."""
        auth_map = {
            "MONGODB-X509": self.auth_radio_buttons.radio_X509,
            "SCRAM-SHA-1": self.auth_radio_buttons.radio_SHA1,
            "MONGODB-AWS": self.auth_radio_buttons.radio_AWS,
            "PLAIN": self.auth_radio_buttons.radio_KERBEROS_2,
            "SCRAM-SHA-256": self.auth_radio_buttons.radio_SHA256,
            "GSSAPI (Kerberos)": self.auth_radio_buttons.radio_KERBEROS,
            "LDAP": self.auth_radio_buttons.radio_LDAP
        }

        for radio_button in auth_map.values():
            radio_button.setChecked(False)

        if auth_type and auth_type in auth_map:
            auth_map[auth_type].setChecked(True)

    def get_selected_auth_type(self) -> str | None:
        """Get the selected authentication type from the UI."""
        return get_selected_auth_type(self.auth_radio_buttons)