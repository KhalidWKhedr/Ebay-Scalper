from src.view.gui.gui_form_database import Ui_form_Database


class SSHPresenter:
    def __init__(
        self,
        ui: Ui_form_Database
    ):
        self.ui = ui

    @staticmethod
    def toggle_elements(elements, visible: bool) -> None:
        for element in elements:
            element.setVisible(visible)

    def toggle_ssh_options(self, is_checked: bool) -> None:
        ssh_elements = [
            self.ui.text_SSH_Host, self.ui.text_SSH_Port, self.ui.text_SSH_Username,
            self.ui.text_SSH_Password, self.ui.label_ssh_host, self.ui.label_ssh_port,
            self.ui.label_ssh_username, self.ui.label_ssh_password
        ]
        self.toggle_elements(ssh_elements, is_checked)
