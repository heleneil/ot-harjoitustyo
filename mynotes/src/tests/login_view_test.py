import unittest
from tkinter import Tk


class TestLoginView(unittest.TestCase):

    def test_login_window_appears(self):
        root = Tk()
        self.assertEqual(root.state(), "normal")
