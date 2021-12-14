import unittest
from unittest.mock import patch
from ui.controller import MyNotesApp
from models.models import User

mock_user_array = [User(55, "eetu")]
mock_written_user = User(55, "joona")


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.my_notes = MyNotesApp()

    def test_validate_login__is_valid(self):
        with patch('ui.controller.read_users_from_file') as mock_read_users:
            mock_read_users.return_value = mock_user_array

            login_validated = self.my_notes.validate_login("eetu")
            self.assertIsNotNone(login_validated)

    def test_validate_login__is_invalid(self):
        with patch('ui.controller.read_users_from_file') as mock_read_users:
            mock_read_users.return_value = mock_user_array

            login_validated = self.my_notes.validate_login("User 55")
            self.assertIsNone(login_validated)

    def test_create_user__user_created(self):
        with patch('ui.controller.write_user_to_file') as mock_write_users:
            mock_write_users.return_value = mock_written_user

            # result is an error msg, or None if a user is created
            result = self.my_notes.create_user("User 6")
            mock_write_users.assert_called_with("User 6")
            self.assertIsNone(result)

    def test_create_user__error_if_short_username(self):
        result = self.my_notes.create_user("Us")
        self.assertEqual("Username too short", result)

    def test_create_user__already_exists(self):
        with patch('ui.controller.read_users_from_file') as mock_read_users:
            mock_read_users.return_value = mock_user_array

            result = self.my_notes.create_user("eetu")
            self.assertEqual("User already exists", result)

    # def test_session_user(self):
