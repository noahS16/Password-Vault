import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import hashlib
from cryptography.fernet import Fernet


class Crypto:
    def __init__(self):
        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'244487',
            iterations=100000,
            backend=default_backend()
        )
        self.encryptionKey = b''

    def hasher(self, txt):
        hashed = hashlib.sha256(txt.encode('utf-8'))
        hashed = hashed.hexdigest()
        return hashed

    def encrypt(self, message: str) -> bytes:
        message = str(message)
        message = message.encode()
        return Fernet(self.encryptionKey).encrypt(message)

    def decrypt(self, message: bytes) -> bytes:
        return Fernet(self.encryptionKey).decrypt(message)

    def set_key(self, key):
        if not self.encryptionKey:
            self.encryptionKey = base64.urlsafe_b64encode(self.kdf.derive(key.encode()))



