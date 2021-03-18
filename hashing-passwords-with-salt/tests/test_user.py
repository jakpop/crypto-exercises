from unittest import TestCase

from src.user import User


class TestUser(TestCase):
    def test_init(self):
        # given
        u = User()

        # when
        u.init('user00', 'haslo')

        # then
        self.assertEqual("user00", u.username)
        self.assertIsNotNone(u.password_salt)
        self.assertIsNotNone(u.password_hash)
