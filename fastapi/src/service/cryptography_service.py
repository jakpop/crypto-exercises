import base64
import logging

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from src.model.asymmetric_key import AsymmetricKey
from src.model.key import Key
from src.service.key_service import KeyService


class CryptographyService:

    key_service: KeyService
    fernet: Fernet

    def __init__(self):
        self.key_service = KeyService()
        self.fernet = Fernet(Fernet.generate_key())
        logging.basicConfig(level=logging.DEBUG)

    def get_symmetric_key(self):
        return Fernet.generate_key()

    def set_symmetric_key(self, key_model: Key):
        self.key_service.set_symmetric_key(key_model.key)

    def encrypt_symmetric(self, message: str) -> bytes:
        return self.fernet.encrypt(data=message.encode())

    def decrypt_symmetric(self, token: bytes) -> bytes:
        return self.fernet.decrypt(token)

    def get_asymmetric_key(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        pub_pem = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        self.key_service.set_asymmetric_private_key(pem)
        self.key_service.set_asymmetric_public_key(pub_pem)

        return {"private_key": pem,
                "public_key": pub_pem}

    def get_asymmetric_key_ssh(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption()
        )
        pub_pem = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH
        )

        self.key_service.set_asymmetric_private_key(pem)
        self.key_service.set_asymmetric_public_key(pub_pem)

        return {"private_key": pem,
                "public_key": pub_pem}

    def set_asymmetric_keys(self, key_model: AsymmetricKey):
        self.key_service.set_asymmetric_public_key(key_model.public_key.encode())
        self.key_service.set_asymmetric_private_key(key_model.private_key.encode())

    def sign_message(self, message: str):
        message = message.encode()
        private_key = self.key_service.get_asymmetric_private_key()
        signature = serialization.load_pem_private_key(private_key, password=None).sign(
            message,
            padding=padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            algorithm=hashes.SHA256()
        )

        return base64.b64encode(signature)

    def verify_message(self, signature: str, message: str):
        public_key = self.key_service.get_asymmetric_public_key()
        serialization.load_pem_public_key(public_key).verify(
            base64.b64decode(signature),
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    def encrypt_asymmetric(self, message: str) -> bytes:
        public_key = self.key_service.get_asymmetric_public_key()
        ciphertext = serialization.load_pem_public_key(public_key).encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return base64.b64encode(ciphertext)

    def decrypt_asymmetric(self, ciphertext: bytes) -> bytes:
        private_key = self.key_service.get_asymmetric_private_key()
        plaintext = serialization.load_pem_private_key(private_key, password=None).decrypt(
            base64.b64decode(ciphertext),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return plaintext
