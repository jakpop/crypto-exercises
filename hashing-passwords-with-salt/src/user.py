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
        self.password_hash = hl.sha256((password + self.password_salt).encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        return hl.sha256((password + self.password_salt).encode()).hexdigest() == self.password_hash



