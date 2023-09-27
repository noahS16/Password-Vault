import pyperclip
from PyQt5.QtWidgets import QMessageBox

from backend.functionality.vault import Vault
from PyQt5 import QtWidgets


class AccountTableItem(QtWidgets.QListWidgetItem):
    def __init__(self, account_ID, name, email, pw):
        super().__init__()
        self.account_ID = account_ID
        self.name = name
        self.email = email
        self.pw = pw
        self.vault = Vault()
        self.setText(name)

    def set_vault(self, vault):
        self.vault = vault


class ViewAccountsScreen:
    def __init__(self, ui):
        self.ui = ui
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.tabWidget.tabBarClicked.connect(lambda: self.populate_accounts_table())
        self.ui.accounts_table.clicked.connect(lambda: self.show_account_info())
        self.ui.copy_email_bttn.clicked.connect(lambda: self.copy_to_clipboard())
        self.ui.copy_pw_bttn.clicked.connect(lambda: self.copy_to_clipboard())
        self.ui.edit_acct_bttn.clicked.connect(lambda: self.transform_edit_button_to_save())
        self.ui.delete_acct_bttn.clicked.connect(lambda: self.delete_account_popup())

    def create_table_items(self):
        current_vault = self.ui.vaults_list.currentItem()
        all_accounts = current_vault.vault.load_all_accounts()
        account_table_items = []
        for account in all_accounts:
            account_ID = account[0]
            name, email, pw = account[1], account[2], account[3]
            row = AccountTableItem(account_ID, name, email, pw)
            row.set_vault(current_vault)
            account_table_items.append(row)
        return account_table_items

    def populate_accounts_table(self):
        all_accounts = self.create_table_items()
        self.ui.accounts_table.clear()
        self.ui.accounts_table.setSortingEnabled(False)
        for row in all_accounts:
            self.ui.accounts_table.addItem(row)
        self.ui.accounts_table.setSortingEnabled(True)

    def show_account_info(self):
        current_account = self.ui.accounts_table.currentItem()
        email = current_account.email
        pw = current_account.pw
        self.ui.show_email_edit.setText(email)
        self.ui.show_pw_edit.setText(pw)
        self.update_account_label(current_account.name)

    def edit_account(self):
        current_account = self.ui.accounts_table.currentItem()
        new_email = self.ui.show_email_edit.text()
        new_pw = self.ui.show_pw_edit.text()
        if not new_email or not new_pw:
            self.empty_field_popup()
        else:
            current_account.vault.vault.update_account(current_account.account_ID, new_email, new_pw)
            self.reset_edit_box()
            self.populate_accounts_table()

    def reset_edit_box(self):
        self.update_account_label("Select an account.")
        self.ui.show_email_edit.setText("")
        self.ui.show_pw_edit.setText("")
        self.ui.show_email_edit.setEnabled(False)
        self.ui.show_pw_edit.setEnabled(False)
        self.ui.edit_acct_bttn.clicked.disconnect()
        self.ui.edit_acct_bttn.clicked.connect(lambda: self.transform_edit_button_to_save())
        self.ui.edit_acct_bttn.setText("Edit")


    def transform_edit_button_to_save(self):
        self.ui.edit_acct_bttn.clicked.disconnect()
        self.ui.edit_acct_bttn.setText("Save")
        self.ui.edit_acct_bttn.clicked.connect(lambda: self.edit_account())
        self.ui.show_pw_edit.setEnabled(True)
        self.ui.show_email_edit.setEnabled(True)

    def delete_account(self):
        current_account = self.ui.accounts_table.currentItem()
        current_account.vault.vault.delete_account(current_account.account_ID)
        self.reset_edit_box()
        self.ui.accounts_table.removeItemWidget(current_account)

    def update_account_label(self, text):
        self.ui.current_acct_label.setText(text)


    def copy_to_clipboard(self):
        text = self.ui.accounts_table.currentItem().text()
        pyperclip.copy(text)

    @staticmethod
    def empty_field_popup():
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Empty Fields")
        msg.setText("Fields must not be empty")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.exec_()

    def delete_account_popup(self):
        account = self.ui.accounts_table.currentItem().text()
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Delete?")
        msg.setIcon(QMessageBox.Question)
        msg.setText(f"Delete login data for {account}?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg.buttonClicked.connect(lambda: self.delete_account())
        msg.exec_()


