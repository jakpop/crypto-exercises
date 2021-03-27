from cryptography.fernet import Fernet


class CryptographyService:

    def __init__(self):
        pass

    def get_key(self):
        return Fernet.generate_key()
