import unittest
from password_checker import is_valid_password

class TestPasswordChecker(unittest.TestCase):

    def test_password_length(self):
        self.assertFalse(is_valid_password("short"))

    def test_uppercase_letter(self):
        self.assertFalse(is_valid_password("password1!"))

    def test_valid_password(self):
        self.assertTrue(is_valid_password("Valid1!"))

if __name__ == '__main__':
    unittest.main()