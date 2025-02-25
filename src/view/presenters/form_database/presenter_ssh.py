class SSHPresenter:
    """Handles SSH-related UI interactions."""

    def __init__(
        self,
        ssh_host_field, ssh_port_field, ssh_username_field, ssh_password_field,
        ssh_host_label, ssh_port_label, ssh_username_label, ssh_password_label
    ):
        self.ssh_host_field = ssh_host_field
        self.ssh_port_field = ssh_port_field
        self.ssh_username_field = ssh_username_field
        self.ssh_password_field = ssh_password_field
        self.ssh_host_label = ssh_host_label
        self.ssh_port_label = ssh_port_label
        self.ssh_username_label = ssh_username_label
        self.ssh_password_label = ssh_password_label

    def toggle_ssh_options(self, is_checked: bool) -> None:
        """Toggle visibility of SSH-related UI elements."""
        elements = [
            self.ssh_host_field, self.ssh_port_field, self.ssh_username_field,
            self.ssh_password_field, self.ssh_host_label, self.ssh_port_label,
            self.ssh_username_label, self.ssh_password_label
        ]
        for element in elements:
            element.setVisible(is_checked)