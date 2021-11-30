import tkinter as tk
from tkinter import Tk, ttk


class CreateUser(tk.Frame):
    reference_frames = {}
    reference_functions = {}

    def init_data(self, reference_frames, reference_functions):
        self.reference_frames = reference_frames
        self.reference_functions = reference_functions

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        title_label = ttk.Label(master=self, text="Create user")
        title_label.grid(row=0, column=0, columnspan=2)

        name_label = ttk.Label(master=self, text="Name:")
        username_label = ttk.Label(master=self, text="Username:")

        name_label.grid(row=1, column=1)
        username_label.grid(row=2, column=1)

        name_field = ttk.Entry(master=self)
        username_field = ttk.Entry(master=self)

        name_field.grid(row=1, column=2)
        username_field.grid(row=2, column=2)

        create_button = ttk.Button(
            self,
            text="Create",
            command=lambda: self.create_user_and_switch_page(
                controller,
                username_field.get()
            )
        )

        create_button.grid(row=3, column=0, columnspan=2)

    def create_user_and_switch_page(self, controller, username):
        user_created = self.reference_functions['create_user'](
            username)
        if user_created:
            controller.show_frame(
                self.reference_frames['home_view_instance']
                )
