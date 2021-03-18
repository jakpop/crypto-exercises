from src.db_controller import DbController
from src.user import User


class UserService(object):

    def __init__(self, db: DbController):
        self.db = db

    def login(self, username: str, password: str) -> str:
        user = self.db.get_user_by_username(username)
        if user.check_password(password=password):
            return f'{user.username} login successful'
        else:
            return 'Password incorrect, try again'

    def register(self, user: User) -> User:
        user_return = self.db.insert_user(user=user)
        return user_return


