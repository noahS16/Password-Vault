import string

from backend.functionality.vault import Vault
import random
from PyQt5 import QtWidgets


class AddAccountScreen:
    def __init__(self, ui):
        self.ui = ui
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.back_to_select_bttn.clicked.connect(lambda: self.go_to_vault_screen())
        self.ui.add_acct_bttn.clicked.connect(lambda: self.add_new_account())
        self.ui.generate_pw_bttn.clicked.connect(lambda: self.generate_pw())

    def get_typed_account(self):
        return self.ui.account_name_edit.text()

    def get_typed_email(self):
        return self.ui.email_eddit.text()

    def get_typed_pw(self):
        return self.ui.acct_pw_edit.text()

    def get_account_input(self):
        return [self.get_typed_account(), self.get_typed_email(), self.get_typed_pw()]

    def get_length_option(self):
        return self.ui.pw_length_edit.value()

    def get_numbers_checked(self):
        return self.ui.numbers_chkbox.isChecked()

    def get_special_chars_checked(self):
        return self.ui.special_char_chkbox.isChecked()

    def get_uppercase_checked(self):
        return self.ui.uppercase_chkbox.isChecked()

    def get_gen_settings(self):
        return [self.get_length_option(), self.get_numbers_checked(), self.get_special_chars_checked(),
                self.get_uppercase_checked()]

    def empty_fields(self):
        return not self.ui.account_name_edit.text() or not self.ui.email_eddit.text() or not self.ui.acct_pw_edit.text()

    def add_new_account(self):
        current_account = self.ui.vaults_list.currentItem()
        if self.empty_fields():
            self.empty_field_popup()
        else:
            account, email, pw = self.get_account_input()
            current_account.vault.add_account(current_account.vault.vault_ID, account, email, pw)
            self.reset_fields()

    def reset_fields(self):
        self.ui.account_name_edit.setText("")
        self.ui.email_eddit.setText("")
        self.ui.acct_pw_edit.setText("")

    def go_to_vault_screen(self):
        self.reset_fields()
        self.ui.stackedWidget.setCurrentIndex(0)

    def generate_pw(self):
        length, hasNumbers, hasSpecial, hasUpper = self.get_gen_settings()
        generated_pw = self.generate_password(length, hasNumbers, hasSpecial, hasUpper)
        self.ui.acct_pw_edit.setText(generated_pw)

    @staticmethod
    def generate_password(length, has_numbers, has_special_char, has_uppercase):
        print(length, has_uppercase, has_special_char, has_numbers)
        # Define character sets based on parameters
        characters = string.ascii_lowercase
        if has_uppercase:
            characters += string.ascii_uppercase
        if has_special_char:
            characters += string.punctuation
        if has_numbers:
            print("DFD")
            characters += string.digits

        # Check if the character set is empty
        if not characters:
            return "Invalid parameters: No character set selected."

        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    @staticmethod
    def empty_field_popup():
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Empty Fields")
        msg.setText("Fields must not be empty")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.exec_()

