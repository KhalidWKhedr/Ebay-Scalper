from src.view.gui.gui_form_database import Ui_form_Database


class SSHPresenter:
    def __init__(
        self,
        ui: Ui_form_Database
    ):
        self.ui = ui

    def toggle_ssh_options(self, is_checked: bool) -> None:
        """Toggle visibility of SSH options based on checkbox."""
        ssh_elements = [
            self.ui.text_SSH_Host, self.ui.text_SSH_Port, self.ui.text_SSH_Username,
            self.ui.text_SSH_Password, self.ui.label_ssh_host, self.ui.label_ssh_port,
            self.ui.label_ssh_username, self.ui.label_ssh_password
        ]
        for element in ssh_elements:
            element.setVisible(is_checked)