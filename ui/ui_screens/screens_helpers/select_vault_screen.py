from PyQt5.QtWidgets import QListWidgetItem, QStyledItemDelegate, QWidget, QListWidget
from PyQt5 import QtWidgets
from backend.functionality.vault import Vault


class VaultListItem(QListWidgetItem):
    def __init__(self, vault: Vault):
        super().__init__()
        self.vault = vault
        self.setText(vault.name)


class SelectVaultScreen:
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.connect_buttons()
        self.populate_vault_list()

    def connect_buttons(self):
        self.ui.add_vault_bttn.clicked.connect(lambda: self.go_to_new_vault_screen())
        self.ui.login_button.clicked.connect(lambda: self.process_login())
        self.ui.delete_vault_bttn.clicked.connect(lambda: self.delete_vault())

    def get_selected_vault(self):
        return self.ui.vaults_list.currentItem()

    def get_typed_pw(self):
        return self.ui.login_edit.text()

    def go_to_new_vault_screen(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def add_vault_to_list(self, list_item: VaultListItem):
        self.ui.vaults_list.addItem(list_item)

    def create_vault_list_items(self, saved_vaults):
        vault_items = []
        for vault in saved_vaults:
            vault_id, name = vault[0], vault[1]
            vault = Vault(name=name, vault_ID=vault_id)
            vault_items.append(VaultListItem(vault))
        return vault_items

    def populate_vault_list(self):
        self.ui.vaults_list.clear()
        saved_vaults = Vault.load_all_vaults()
        list_items = self.create_vault_list_items(saved_vaults)
        for item in list_items:
            self.add_vault_to_list(item)

    def process_login(self):
        pw_attempt = self.get_typed_pw()
        selected_vault = self.get_selected_vault()
        if selected_vault.vault.login(pw_attempt):
            self.go_to_home_screen()
        else:
            self.show_invalid_login_popup()

    def delete_vault(self):
        current_vault = self.ui.vaults_list.currentItem()
        current_vault.vault.delete_vault()
        self.populate_vault_list()

    def go_to_home_screen(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def show_invalid_login_popup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Uh Oh!")
        msg.setText("Invalid Password")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()

