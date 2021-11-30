import unittest
from ui.views import validate_login


class TestLogin(unittest.TestCase):

    def test_login_valid(self):
        login_validated = validate_login("User 2")
        self.assertTrue(login_validated)

    def test_login_invalid(self):
        login_validated = validate_login("User 4")
        self.assertFalse(login_validated)
