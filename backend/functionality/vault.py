import random
from .key import Crypto
from backend.db import db
import pyperclip


class Vault:
    def __init__(self, name=None, vault_ID=None):
        self.name = name
        self.vault_ID = vault_ID
        self.crypto = Crypto()

    def add_vault(self, pw, name, email):
        self.crypto.set_key(pw)
        pw = self.crypto.hasher(pw)
        db.add_vault(name, email, pw)
        vault_ID = db.get_vault_id(name)
        print("ID:", vault_ID, name)
        self.vault_ID = vault_ID
        return vault_ID

    def login(self, password):
        saved = db.get_vault_password(self.vault_ID)
        saved = saved[0][0]
        if saved == self.crypto.hasher(password):
            self.crypto.set_key(password)
            return True
        return False

    @staticmethod
    def load_all_vaults():
        vaults = db.get_vaults()
        return vaults

    def load_all_accounts(self):
        data = db.get_user_accounts(self.vault_ID)
        rows = []
        for i in range(len(data)):
            rows.append([data[i][0],
                         self.crypto.decrypt(data[i][2]).decode(),
                         self.crypto.decrypt(data[i][3]).decode(),
                         self.crypto.decrypt(data[i][4]).decode()])
        rows.sort()
        return rows

    def add_account(self, vault_ID, account, email, pw):
        account = self.crypto.encrypt(account)
        email = self.crypto.encrypt(email)
        pw = self.crypto.encrypt(pw)
        db.add_account(vault_ID, account, email, pw)

    def update_account(self, accountID, username, pw):
        username = self.crypto.encrypt(username)
        pw = self.crypto.encrypt(pw)
        db.update_account(self.vault_ID, accountID, username, pw)

    def delete_account(self, account_ID):
        db.delete_account(self.vault_ID, account_ID)

    def delete_vault(self):
        db.delete_vault(self.vault_ID)

