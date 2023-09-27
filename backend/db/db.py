import sqlite3

db_name = "backend/db/mydb.db"


def setup_db():
    db, cursor = connect_db()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vault (
    vault_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(50),
    email varchar(50),
    password varchar(50))
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Account (
    account_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    vault_ID INTEGER,
    site_name varchar(50),
    username varchar(50),
    password varchar(50),
    FOREIGN KEY (vault_ID) REFERENCES Vault(vault_ID))
    """)
    db.commit()


def connect_db():
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    return db, cursor


def close_db(db, cursor):
    db.close()
    cursor.close()
    return


def add_vault(name, email, user_password):
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    query = "INSERT INTO Vault(name, email, password) VALUES(?, ?, ?)"
    cursor.execute(query, (name, email, user_password))
    db.commit()
    # self.close_db(db, cursor)


def add_account(vault_ID, account, email, password):
    db, cursor = connect_db()
    query = "INSERT INTO Account (vault_ID, site_name, username, password) VALUES(?, ?, ?, ?)"
    cursor.execute(query, (vault_ID, account, email, password))
    db.commit()
    # self.close_db(db, cursor)


def delete_account(vault_ID, account_ID):
    db, cursor = connect_db()
    query = "DELETE FROM Account WHERE vault_ID=? AND account_ID=?"
    cursor.execute(query, (vault_ID, account_ID))
    db.commit()
    # self.close_db(db, cursor)


def delete_vault(vault_ID):
    db, cursor = connect_db()
    query = "DELETE FROM Vault WHERE vault_ID=?"
    cursor.execute(query, (vault_ID,))
    query = "DELETE From Account WHERE vault_ID=?"
    cursor.execute(query, (vault_ID,))
    db.commit()
    # self.close_db(db, cursor)


# Return true if user table is empty (i.e, first login)
def vaults_empty():
    db, cursor = connect_db()
    cursor.execute("SELECT * FROM Vault")
    empty = cursor.fetchall()
    # self.close_db(db, cursor)
    return not empty


# Return true if accounts table is empty
def accounts_empty():
    db, cursor = connect_db()
    cursor.execute("SELECT * FROM Account")
    empty = cursor.fetchall()
    # self.close_db(db, cursor)
    return not empty


def get_user_accounts(vault_ID):
    db, cursor = connect_db()
    query = "SELECT * FROM Account WHERE vault_ID=?"
    cursor.execute(query, (vault_ID,))
    data = cursor.fetchall()
    # self.close_db(db, cursor)
    return data


def get_vaults():
    db, cursor = connect_db()
    cursor.execute("SELECT * FROM Vault")
    data = cursor.fetchall()
    # self.close_db(db, cursor)
    return data


def get_vault_password(vault_ID):
    db, cursor = connect_db()
    query = "SELECT password FROM Vault WHERE vault_ID=?"
    cursor.execute(query, (vault_ID,))
    password = cursor.fetchall()
    # self.close_db(db, cursor)
    return password


def get_vault_id(name):
    db, cursor = connect_db()
    query = "SELECT vault_ID FROM Vault WHERE name=?"
    cursor.execute(query, (name,))
    user_ID = cursor.fetchall()
    # self.close_db(db, cursor)
    return user_ID[0][0]


def getName():
    db = sqlite3.connect("tester.db")
    cursor = db.cursor()
    cursor.execute("SELECT customer FROM master")
    name = cursor.fetchall()
    cursor.close()
    db.close()
    return name


def update_account(vault_ID, account_ID, username, password):
    print("account, vault:", account_ID, vault_ID)
    db, cursor = connect_db()
    query = """
        UPDATE Account
        SET 
        username=? , password=?
        WHERE account_ID=? AND vault_ID=?
    """
    cursor.execute(query, (username, password, account_ID, vault_ID))
    db.commit()
    # self.close_db(db, cursor)
