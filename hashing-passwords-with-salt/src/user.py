import hashlib as hl
import string
import random
from typing import Optional


class User(object):

    username: Optional[str]
    password_salt: Optional[str]
    password_hash: Optional[str]

    def __init__(self):
        pass

    def init(self, username: str, password: str) -> None:
        self.username = username
        self.password_salt = ''.join(random.choices(string.ascii_lowercase + string.digits, k=32))
        self.password_hash = hl.pbkdf2_hmac('sha256', password.encode(), self.password_salt.encode(), 100000).hex()

    def check_password(self, password: str) -> bool:
        return hl.pbkdf2_hmac('sha256', password.encode(), self.password_salt.encode(), 100000).hex() == self.password_hash
