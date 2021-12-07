import unittest
from ui.controller import MyNotesApp


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.my_notes = MyNotesApp()

    def test_login_valid(self):
        login_validated = self.my_notes.validate_login("User 2")
        self.assertIsNotNone(login_validated)

    def test_login_invalid(self):
        login_validated = self.my_notes.validate_login("User 4")
        self.assertIsNone(login_validated)
