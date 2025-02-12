def get_selected_auth_type(ui) -> str | None:
    """Get the selected authentication type from radio buttons."""
    auth_map = {
        ui.radio_X509: "MONGODB-X509",
        ui.radio_SHA1: "SCRAM-SHA-1",
        ui.radio_AWS: "MONGODB-AWS",
        ui.radio_KERBEROS_2: "PLAIN",
        ui.radio_SHA256: "SCRAM-SHA-256",
        ui.radio_KERBEROS: "GSSAPI (Kerberos)",
        ui.radio_LDAP: "LDAP"
    }

    for radio_button, auth_value in auth_map.items():
        if radio_button.isChecked():
            return auth_value
    return None
