from ui.ui_files.main_ui import Ui_HomeWindow
from backend.functionality.vault import Vault
from PyQt5 import QtWidgets
from .select_vault_screen import VaultListItem


class NewVaultScreen:
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.create_button.clicked.connect(lambda: self.create_vault())
        self.ui.back_button.clicked.connect(lambda: self.go_to_vault_select())

    def get_new_name(self):
        return self.ui.new_name_edit.text()

    def get_new_email(self):
        return self.ui.new_email_edit.text()

    def get_new_pw(self):
        return self.ui.new_pw_edit.text()

    def fields_empty(self):
        return not self.ui.new_name_edit.text() or not self.ui.new_email_edit.text() or not self.ui.new_pw_edit.text()

    def create_vault(self):
        if not self.fields_empty():
            name = self.get_new_name()
            email = self.get_new_email()
            pw = self.get_new_pw()
            new_vault = Vault(name=name)
            new_vault.add_vault(pw, name, email) # to db
            vault_list_item = VaultListItem(new_vault)
            self.ui.vaults_list.addItem(vault_list_item)
            self.go_to_vault_select()
        else:
            self.empty_field_popup()
            return False

    def go_to_vault_select(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.clear_form()

    def clear_form(self):
        self.ui.new_name_edit.setText("")
        self.ui.new_email_edit.setText("")
        self.ui.new_pw_edit.setText("")

    @staticmethod
    def empty_field_popup():
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Empty Fields")
        msg.setText("Fields must not be empty")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.exec_()


