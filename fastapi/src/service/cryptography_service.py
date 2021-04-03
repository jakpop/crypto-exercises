from cryptography.fernet import Fernet

from src.model.Key import Key
from src.service.key_service import KeyService


class CryptographyService:

    key_service: KeyService
    fernet: Fernet

    def __init__(self):
        self.key_service = KeyService()
        self.fernet = Fernet(Fernet.generate_key())

    def get_symmetric_key(self):
        return Fernet.generate_key()

    def set_symmetric_key(self, key_model: Key):
        self.key_service.set_symmetric_key(key_model.key)

    def encrypt_symmetric(self, message: str) -> bytes:
        return self.fernet.encrypt(data=message.encode())

    def decrypt_symmetric(self, token: bytes) -> bytes:
        return self.fernet.decrypt(token)


