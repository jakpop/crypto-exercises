import sqlite3
from unittest import TestCase
from unittest.mock import patch

import mockito
from mockito import when, verifyNoUnwantedInteractions

from src.user import User
from src.user_service import UserService
from src.db_controller import DbController


class TestUserService(TestCase):

    def test_login_correct(self):
        # given
        con = sqlite3.connect('mock_db')
        cur = con.cursor()
        db = DbController(con, cur)
        us = UserService(db)

        u = User()
        u.username = "user00"
        u.password = "haslo"
        u.password_salt = "z4ub8qtepmwfkdr467itjpisip1wsv05"
        u.password_hash = "629a07bcbb353e679b906bbd17294c97d88c194d731384edbf9fd9f00783ff10"

        # when
        when(db).get_user_by_username('user00').thenReturn(u)
        when(u).check_password(password='haslo').thenReturn(True)
        result = us.login(u.username, u.password)

        # then
        verifyNoUnwantedInteractions(db.get_user_by_username('user00'))
        self.assertEqual('user00 login successful', result)

    def test_login_incorrect(self):
        # given
        con = sqlite3.connect('mock_db')
        cur = con.cursor()
        db = DbController(con, cur)
        us = UserService(db)

        u = User()
        u.username = "user00"
        u.password = "haslo"
        u.password_salt = "z4ub8qtepmwfkdr467itjpisip1wsv05"
        u.password_hash = "629a07bcbb353e679b906bbd17294c97d88c194d731384edbf9fd9f00783ff10"

        # when
        when(db).get_user_by_username('user00').thenReturn(u)
        when(u).check_password(password='haslo').thenReturn(False)
        result = us.login(u.username, u.password)

        # then
        verifyNoUnwantedInteractions(db.get_user_by_username('user00'))
        self.assertEqual('Password incorrect, try again', result)

    def test_register(self):
        # given
        con = sqlite3.connect('mock_db')
        cur = con.cursor()
        db = DbController(con, cur)
        us = UserService(db)

        u = User()
        u.username = "user00"
        u.password = "haslo"

        u2 = User()
        u2.password_salt = "z4ub8qtepmwfkdr467itjpisip1wsv05"
        u2.password_hash = "629a07bcbb353e679b906bbd17294c97d88c194d731384edbf9fd9f00783ff10"

        # when
        when(db).insert_user(user=u).thenReturn(u2)
        result = us.register(u)

        # then
        self.assertEqual('629a07bcbb353e679b906bbd17294c97d88c194d731384edbf9fd9f00783ff10', result.password_hash)
