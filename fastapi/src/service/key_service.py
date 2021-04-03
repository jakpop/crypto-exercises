from typing import Optional


class KeyService:

    latest_symmetric: Optional[str]
    latest_asymmetric: Optional[str]

    def __init__(self):
        self.latest_symmetric = None
        self.latest_asymmetric = None

    def get_symmetric_key(self) -> str:
        return self.latest_symmetric

    def set_symmetric_key(self, key: str):
        self.latest_symmetric = key

    def get_asymmetric_key(self) -> str:
        return self.latest_asymmetric

    def set_asymmetric_key(self, key: str):
        self.latest_asymmetric = key
