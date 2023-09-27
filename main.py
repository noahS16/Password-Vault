import sys
from PyQt5 import QtWidgets
from ui.ui_files.main_ui import Ui_HomeWindow
from ui.ui_screens.screens_helpers.select_vault_screen import SelectVaultScreen
from ui.ui_screens.screens_helpers.new_vault_screen import NewVaultScreen
from ui.ui_screens.screens_helpers.add_acct_screen import AddAccountScreen
from ui.ui_screens.screens_helpers.view_accounts_screen import ViewAccountsScreen
from backend.db import db


class Runner:
    def __init__(self, ui):
        db.setup_db()
        SelectVaultScreen(ui)
        NewVaultScreen(ui)
        AddAccountScreen(ui)
        ViewAccountsScreen(ui)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    HomeWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(HomeWindow)
    Runner(ui)
    HomeWindow.show()
    sys.exit(app.exec_())

