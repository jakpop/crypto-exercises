import logging
import sqlite3
from collections import namedtuple

from src.user import User


class DbController(object):

    con: sqlite3.Connection
    cur: sqlite3.Cursor

    def __init__(self, db: sqlite3.Connection, cur: sqlite3.Cursor):
        self.con = db
        self.cur = cur

    def create_table(self) -> None:
        """ Creates a new table if it does not exist. """

        self.cur = self.con.cursor()
        try:
            self.cur.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='passwords' ''')
            if self.cur.fetchone()[0] == 0:
                print("Password table does not exists, creating now")
                self.con.execute('''CREATE TABLE passwords (username text, password_salt text, password text)''')
            self.con.commit()
        except Exception as e:
            raise self.con.DatabaseError(f"Couldn't create new table: {str(e)}")

    def insert_user(self, user: User) -> User:
        """
        Add user to the database.
        :param user: User object to be inserted
        :return: the same user object passed as an argument
        """

        try:
            query = f'''INSERT INTO passwords (username, password_salt, password) 
                        VALUES ('{user.username}','{user.password_salt}','{user.password_hash}')'''
            self.cur.execute(query)
            self.con.commit()
        except Exception as e:
            raise self.con.DatabaseError(f"Couldn't create new user: {str(e)}")
        return user

    def show_users(self) -> None:
        """ Fetch all records from the table """

        try:
            allrows = self.cur.execute('''SELECT * FROM passwords''').fetchall()
            for row in allrows:
                print(row)
            self.con.commit()
        except Exception as e:
            raise self.con.DatabaseError(f"Couldn't fetch users: {str(e)}")

    def get_user_by_username(self, username: str) -> User:
        """
        Get user by username.
        :param username: username of the user to be fetched
        :rtype: User
        """

        UserRecord = namedtuple('UserRecord', 'username, password_salt, password')

        query = f'''SELECT username, password_salt, password from passwords WHERE username = '{username}' '''
        try:
            self.cur.execute(query)
            user = User()
            for user_fetched in map(UserRecord._make, self.cur.fetchall()):
                user.username = user_fetched.username
                user.password_salt = user_fetched.password_salt
                user.password_hash = user_fetched.password
            self.con.commit()
        except Exception as e:
            raise self.con.DatabaseError(f'User does not exist: {str(e)}')

        return user
