from src.db_controller import DbController
from src.user import User


class UserService(object):

    db: DbController

    def __init__(self, db: DbController):
        self.db = db

    def login(self, username: str, password: str) -> str:
        """
        Log in user. Gets user from database by username and then checks if password is correct.
        :param username: username of the user wanting to log in
        :param password: password of the user wanting to log in
        :return: login message
        """
        user = self.db.get_user_by_username(username)
        if user.check_password(password=password):
            return f'{user.username} login successful'
        else:
            return 'Password incorrect, try again'

    def register(self, user: User) -> User:
        """
        Register user. Inserts user to database.
        :param user: User object to register
        :return: the same user object passed as an argument
        """
        user_return = self.db.insert_user(user=user)
        return user_return


