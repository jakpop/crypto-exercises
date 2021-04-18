from unittest import TestCase

from cryptography.fernet import InvalidToken
from fastapi import HTTPException
from mockito import when

from src.model.key import Key
from src.service.cryptography_service import CryptographyService


class TestCryptographyService(TestCase):
    def test_get_symmetric_key(self):
        # given
        cs = CryptographyService()

        # when
        when(cs.fernet).generate_key().thenReturn("key")
        result = cs.get_symmetric_key()

        # then
        self.assertEqual("key", result)

    def test_set_symmetric_key(self):
        # given
        cs = CryptographyService()
        k = Key(key="key")

        # when
        cs.set_symmetric_key(k)

        # then
        self.assertEqual("key", cs.key_service.get_symmetric_key())

    def test_encrypt_symmetric(self):
        # given
        cs = CryptographyService()
        message = "hello world"

        # when
        when(cs.fernet).encrypt(data=message.encode()).thenReturn("encrypted message")
        result = cs.encrypt_symmetric(message)

        # then
        self.assertEqual("encrypted message", result)

    def test_decrypt_symmetric(self):
        # given
        cs = CryptographyService()
        token = b"encrypted message"

        # when
        when(cs.fernet).decrypt(token).thenReturn("hello world")
        result = cs.decrypt_symmetric(token)

        # then
        self.assertEqual("hello world", result)

    def test_decrypt_symmetric_exception(self):
        # given
        cs = CryptographyService()
        token = b"encrypted message"

        # when
        when(cs.fernet).decrypt(token).thenRaise(InvalidToken)

        # then
        self.assertRaises(HTTPException, cs.decrypt_symmetric, token)
