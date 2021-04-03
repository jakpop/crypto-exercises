from typing import Optional


class KeyService:

    latest_symmetric: Optional[str]
    latest_asymmetric_private: Optional[bytes]
    latest_asymmetric_public: Optional[bytes]

    def __init__(self):
        self.latest_symmetric = None
        self.latest_asymmetric_private = None
        self.latest_asymmetric_public = None

    def get_symmetric_key(self) -> str:
        return self.latest_symmetric

    def set_symmetric_key(self, key: str):
        self.latest_symmetric = key

    def get_asymmetric_private_key(self) -> bytes:
        return self.latest_asymmetric_private

    def set_asymmetric_private_key(self, key: bytes):
        self.latest_asymmetric_private = key

    def get_asymmetric_public_key(self) -> bytes:
        return self.latest_asymmetric_public

    def set_asymmetric_public_key(self, key: bytes):
        self.latest_asymmetric_public = key
