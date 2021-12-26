import unittest

from models.models import Note, User, delete_note_from_file, delete_user_from_file, read_notes_from_file, read_notes_from_file_for_user, read_users_from_file, update_note_in_file, write_note_to_file, write_user_to_file


class TestModels(unittest.TestCase):
    mock_user = User(99999, "MOCK USER 99999")

    mock_notes = [
        Note(99990, "title 99990", "content 99990", mock_user.id),
        Note(99991, "title 99991", "content 99991", mock_user.id),
        Note(99992, "title 99992", "content 99992", mock_user.id),
    ]

    def setUp(self):
        self.mock_user = write_user_to_file(self.mock_user.username)
        for idx, note in enumerate(self.mock_notes):
            self.mock_notes[idx].user_id = self.mock_user.id
            self.mock_notes[idx] = write_note_to_file(note)

    def tearDown(self):
        returned_notes = read_notes_from_file_for_user(self.mock_user)
        for note in returned_notes:
            delete_note_from_file(note)
        delete_user_from_file(self.mock_user)

    def assert_user_is_equal(self, user_1, user_2):
        self.assertEqual(user_1.username, user_2.username)

    def assert_note_is_equal(self, note_1, note_2):
        self.assertEqual(note_1.title, note_2.title)
        self.assertEqual(note_1.content, note_2.content)
        self.assertEqual(note_1.user_id, note_2.user_id)

    def assert_user_in(self, user_1, users):
        for user in users:
            if user.username == user_1.username:
                self.assert_user_is_equal(user_1, user)
                return
        self.assertTrue(False)

    def assert_note_in(self, note_list_1, note_list_2):
        titles = [o.title for o in note_list_1]
        contents = [o.content for o in note_list_1]
        user_ids = [o.user_id for o in note_list_1]

        for note in note_list_2:
            if note.title in titles and note.content in contents and note.user_id in user_ids:
                self.assertTrue(True)
                return
        self.assertTrue(False)

    def assert_note_not_in(self, note_1, note_list_2):
        found = False

        for note in note_list_2:
            if note.title == note_1.title and note.content == note_1.content and note.user_id == note_1.user_id:
                found = True
        self.assertFalse(found)

    def test_read_users_from_file__users_returned(self):
        self.assert_user_in(self.mock_user, read_users_from_file())

    def test_write_user_to_file__user_returned(self):
        user_created = write_user_to_file(self.mock_user.username)

        self.assert_user_is_equal(self.mock_user, user_created)
        delete_user_from_file(user_created)

    def test_read_notes_from_file__notes_returned(self):
        self.assert_note_in(self.mock_notes, read_notes_from_file())

    def test_read_notes_from_file_for_user__notes_returned(self):
        self.assert_note_in(
            self.mock_notes,
            read_notes_from_file_for_user(self.mock_user)
        )

    def test_write_note_to_file__note_returned(self):
        note = Note(99993, "title 99993", "content 99993", self.mock_user.id)
        created_note = write_note_to_file(note)

        self.assert_note_is_equal(created_note, note)

    def test_delete_note_from_file__note_deleted(self):
        delete_note_from_file(self.mock_notes[2])

        self.assert_note_not_in(
            self.mock_notes[2],
            read_notes_from_file_for_user(self.mock_user)
        )

    def test_update_note_in_file__note_returned(self):
        note = self.mock_notes[2]
        note.title = "a new title"
        updated_note = update_note_in_file(note)

        self.assert_note_is_equal(updated_note, note)
