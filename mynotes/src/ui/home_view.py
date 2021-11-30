import tkinter as tk
from tkinter import Tk, ttk


class Home(tk.Frame):
    users = []
    notes = []
    reference_frames = {}
    reference_functions = {}

    def init_data(self, users, notes):
        self.users = users
        self.notes = notes

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        title_label = ttk.Label(master=self, text="MyNotes")

        title_label.grid(row=0, column=0, columnspan=2)

        create_note_button = ttk.Button(master=self, text="New note")

        create_note_button.grid(row=3, column=0, columnspan=2)

        # making sure notes mock data is initialized
        test_notes_exist = ttk.Label(
            master=self,
            text=f"The first note is: {self.notes[0].title}"
        )
        test_notes_exist.grid(row=4, column=0, columnspan=2)
