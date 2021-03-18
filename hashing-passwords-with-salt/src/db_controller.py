import sqlite3

from src.user import User


class DbController(object):

    def __init__(self, db: sqlite3.Connection, cur: sqlite3.Cursor):
        self.con = db
        self.cur = cur

    def create_table(self) -> None:
        self.cur = self.con.cursor()

        try:
            self.cur.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='passwords' ''')
            if self.cur.fetchone()[0] == 0:
                print("Password table does not exists, creating now")
                self.con.execute('''CREATE TABLE passwords (username text, password_salt text, password text)''')
            self.con.commit()
        except:
            raise self.con.DatabaseError("Couldn't create new table")

    def insert_user(self, user: User) -> User:
        try:
            query = ''' INSERT INTO passwords (username, password_salt, password) VALUES ('{}','{}','{}')'''
            query = query.format(user.username, user.password_salt, user.password_hash)
            self.cur.execute(query)
            self.con.commit()
        except:
            raise self.con.DatabaseError("Couldn't create new user")
        return user

    def show_users(self) -> None:
        try:
            allrows = self.cur.execute('''SELECT * FROM passwords''').fetchall()
            for row in allrows:
                print(row)
            self.con.commit()
        except:
            raise self.con.DatabaseError("Couldn't fetch users")

    def get_user_by_username(self, username: str) -> User:
        query = '''SELECT username, password_salt, password from passwords WHERE username = '{}' '''
        query = query.format(username)
        result = self.cur.execute(query).fetchall()
        try:
            user = User()
            user.username = result[0][0]
            user.password_salt = result[0][1]
            user.password_hash = result[0][2]
            self.con.commit()
        except:
            raise self.con.DatabaseError('User does not exist')

        return user
