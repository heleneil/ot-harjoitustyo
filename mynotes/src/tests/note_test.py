import unittest
from ui.controller import MyNotesApp


class NoteTest(unittest.TestCase):
    def setUp(self):
        self.my_notes = MyNotesApp()

        # def create_note_works(self):
