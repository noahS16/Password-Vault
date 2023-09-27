# Encrypted Password Saver (Desktop app)

---
## This is a Desktop App made using python that I made to help make saving site login information safe, and more efficient than the built-in password saver in most browsers.

While using my browser, I would often find that login information that I had entered had never been stored in the browser's default password saver.
This would lead me to constantly having to reset my passwords and updating them, just to find that they had yet again not been stored. I decided to make my own version to avoid such problems.


---
## Functionality
* Main functionality and features of this program includes:
  * Create one or multiple password-secured vaults, each with their own separate data.
  * Generate passwords with options to choose from such as password length, special characters, etc.
  * Update or edit passwords/login
  * SHA-256 hashing for user-password storage 
  * Encryption on website data storage.

---
## Installation
* ### Dependencies:
  * The following libraries will need to be installed to run this app (installation instructions below):
    * [Cryptography](https://pypi.org/project/cryptography/)
    * [PyQt5](https://pypi.org/project/pyqt5-tools/)
    * [Pyperclip](https://pypi.org/project/pyperclip/)
  * From the command line, run ```pip3 install --upgrade -r requirements.txt```.
* ### Run:
  * Clone this repository in an empty directory.
  * From the command line, navigate to the project file, then run ```python3 main.py```.

---
## To Use
* ### Create a Vault:
  * Select the add vault button from the start screen.
  * Fill out the required fields, then click create.
  * Remember the password you typed, this will be needed each time you access the vault
* ### Add accounts:
  * After logging in to a vault, fill out the required fields in the "Add" tab.
  * Configure password options if generating a password, otherwise continue to fill in a password for the account being added.
  * Click "Add account"
* ### View accounts:
  * Click the "View" tab at the top. Saved accounts be listed on the left.
  * Select an account to view login information
  * Click the "copy" buttons to copy the email or password to your clipboard.
  * "Delete" will delete the selected account
* ### Edit accounts:
  * Click on the "Edit" button on the bottom right in the "View" tab
  * Edit the desired fields.
  * Click the "Save" button on bottom right.

---
## License
This project is licensed under the MIT license.
