import unittest
from unittest.mock import patch
from ui.controller import MyNotesApp
from models.models import Note


mock_note_array = [Note(50, 'Note 50 title', 'This is my 50th note', 10)]
mock_written_note = Note(62, 'Shopping list', 'bananas, bread', 15)


class TestNote(unittest.TestCase):
    def setUp(self):
        self.my_notes = MyNotesApp()

    def test_create_note__note_created(self):
        with patch('ui.controller.write_note_to_file') as mock_write_notes:
            mock_write_notes.return_value = mock_written_note

            result = self.my_notes.create_or_update_note(
                Note(None, None, None, None))
            self.assertEqual(result, mock_written_note)

    def test_set_session_note__session_note_set(self):
        self.my_notes.set_session_note(mock_written_note)

        self.assertEqual(self.my_notes.session_note, mock_written_note)

    def test_set_notes__notes__are_set(self):
        self.my_notes.set_notes(mock_note_array)

        self.assertEqual(self.my_notes.get_notes(), mock_note_array)

    def test_get_notes__no_loaded_notes__file_is_read(self):
        with patch('ui.controller.read_notes_from_file_for_user') as mock_read_notes:
            mock_read_notes.return_value = mock_note_array

            self.assertEqual(self.my_notes.get_notes(), mock_note_array)

    def test_get_notes__loaded_notes_exist__file_is_not_read(self):
        with patch('ui.controller.read_notes_from_file_for_user') as mock_read_notes:
            mock_read_notes.return_value = mock_note_array

            manual_loaded_notes = [Note(20, "Big title", "long content", 50)]
            self.my_notes.set_notes(manual_loaded_notes)

            self.assertEqual(self.my_notes.get_notes(), manual_loaded_notes)

