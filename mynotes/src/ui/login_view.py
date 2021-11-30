import tkinter as tk
from tkinter import ttk


class Login(tk.Frame):
    reference_frames = {}
    reference_functions = {}

    def init_data(self, reference_frames, reference_functions):
        self.reference_frames = reference_frames
        self.reference_functions = reference_functions

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        # TODO: handle grid through pack()
        title_label = ttk.Label(master=self, text="Log in")

        username_label = ttk.Label(master=self, text="Username")
        username_field = ttk.Entry(master=self)

        login_button = ttk.Button(
            self,
            text="Log In",
            command=lambda: self.validate_and_switch_pages(
                controller,
                username_field.get()
                )
        )

        title_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        username_field.grid(row=1, column=1)

        login_button.grid(row=3, column=0, columnspan=2)

        create_user_button = ttk.Button(
            self,
            text="Create user",
            command=lambda: controller.show_frame(
                self.reference_frames['create_user_instance']
                )
        )

        create_user_button.grid(row=4, column=0, columnspan=2)

    def validate_and_switch_pages(self, controller, username):
        login_validated = self.reference_functions['validate_login'](
            username
            )
        if login_validated:
            controller.show_frame(
                self.reference_frames['home_view_instance']
                )
        else:
            invalid_username_label = ttk.Label(
                master=self, text="Invalid username", foreground='red')
            invalid_username_label.grid(row=2, column=0, columnspan=2)
