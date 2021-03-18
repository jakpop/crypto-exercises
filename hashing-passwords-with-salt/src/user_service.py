from src.db_controller import DbController
from src.user import User


class UserService(object):

    def __init__(self, db: DbController):
        self.db = db

    def login(self, username: str, password: str) -> None:
        user = self.db.get_user_by_username(username)
        if user.check_password(password=password):
            print(f'{user.username} login successful')
        else:
            print('Password incorrect, try again')

    def register(self, username: str, password: str) -> User:
        user = User()
        user.init(username=username, password=password)
        user = self.db.insert_user(user=user)
        return user


