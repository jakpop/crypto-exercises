from unittest import TestCase

from src.Hash import Hash


class TestHash(TestCase):

    def test_hashing(self):
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore " \
               "et dolore magna aliqua. "
        h = Hash()
        result = h.hashing(text)
        self.assertIn("md5", result)
        self.assertNotIn("shake_256", result)

    def test_file_hashing(self):
        path = "../ubuntu-18.04.5-desktop-amd64.iso"
        h = Hash()
        result = h.file_hashing(path)
        self.assertEqual(result, "f295570badb09a606d97ddfc3421d7bf210b4a81c07ba81e9c040eda6ddea6a0")
