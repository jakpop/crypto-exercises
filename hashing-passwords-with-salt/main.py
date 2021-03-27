import sqlite3

from src.db_controller import DbController
from src.user import User
from src.user_service import UserService

if __name__ == '__main__':
    con = sqlite3.connect('users_db')
    cur = con.cursor()
    db = DbController(con, cur)
    us = UserService(db)

    db.create_table()

    print("==REGISTER==")
    username = input('Enter username: ')
    password = input('Enter your password: ')
    password_check = input('Enter your password once again: ')
    print()

    if password == password_check:
        user = User()
        user.init(username=username, password=password)
        us.register(user)
        print('Successfully saved user')
    else:
        print('Password doesnt match')

    print("\n==LOGIN==")
    username = input('Enter username: ')
    password = input('Enter your password: ')
    print(us.login(username, password))
