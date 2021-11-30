import tkinter as tk
from tkinter import ttk


class Login(tk.Frame):
    users = []
    notes = []
    reference_frames = {}
    reference_functions = {}

    def init_data(self, users, notes):
        self.users = users
        self.notes = notes

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        # TODO: handle grid through pack()
        # canvas = tk.Canvas(self, height=HEIGHT, width=WIDTH)
        # canvas.pack()
        title_label = ttk.Label(master=self, text="Log in")

        username_label = ttk.Label(master=self, text="Username")
        username_field = ttk.Entry(master=self)

        login_button = ttk.Button(
            self,
            text="Log In",
            command=lambda: self.validate_and_switch_pages(
                controller,
                username_field.get(),
                self.users
                )
        )

        title_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        username_field.grid(row=1, column=1)

        login_button.grid(row=2, column=0, columnspan=2)

        create_user_button = ttk.Button(
            self,
            text="Create user",
            command=lambda: controller.show_frame(
                self.reference_frames['create_user_instance']
                )
        )

        create_user_button.grid(row=3, column=0, columnspan=2)

    def validate_and_switch_pages(self, controller, username, users):
        login_validated = self.reference_functions['validate_login'](
            username, users
            )
        if login_validated:
            controller.show_frame(
                self.reference_frames['home_view_instance']
                )
        else:
            print("No user with that username.")
