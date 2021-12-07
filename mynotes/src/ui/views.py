import tkinter as tk
from tkinter import ttk


class Login(tk.Frame):
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
            command=lambda: controller.show_frame(CreateUser)
        )

        create_user_button.grid(row=4, column=0, columnspan=2)

    def validate_and_switch_pages(self, controller, username):
        validated_user = controller.validate_login(username)
        if validated_user is not None:
            controller.set_session_user(validated_user)
            controller.show_frame(Home)
        else:
            invalid_username_label = ttk.Label(
                master=self, text="Invalid username", foreground='red')
            invalid_username_label.grid(row=2, column=0, columnspan=2)


class CreateUser(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        title_label = ttk.Label(master=self, text="Create user")
        title_label.grid(row=0, column=0, columnspan=2)

        username_label = ttk.Label(master=self, text="Username:")

        username_label.grid(row=2, column=0, columnspan=2)

        username_field = ttk.Entry(master=self)
        username_field.grid(row=2, column=2, columnspan=2)

        username_error_label = None

        create_button = ttk.Button(
            self,
            text="Create and sign in",
            command=lambda: self.create_user_and_switch_page(
                controller,
                username_field.get(),
                username_error_label,
            )
        )

        create_button.grid(row=4, column=0, columnspan=2)

    def create_user_and_switch_page(
        self,
        controller,
        username,
        username_error_label
    ):
        user_created_error = controller.create_user(username)
        if user_created_error is not None:
            username_error_label = ttk.Label(
                master=self, text=user_created_error, foreground='red')
            username_error_label.grid(row=3, column=0, columnspan=2)
            return

        # if no errors show homepage
        controller.show_frame(Home)


class Home(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        title_label = ttk.Label(
            master=self,
            text=f"MyNotes\nHello {controller.session_user.username}")

        title_label.grid(row=0, column=0, columnspan=2)

        create_note_button = ttk.Button(
            self,
            text="New note",
            command=lambda: controller.show_frame(Note)
        )

        create_note_button.grid(row=3, column=0, columnspan=2)

        for idx, note in enumerate(controller.get_notes()):
            note_label = ttk.Label(
                master=self,
                text=f"{note.title}\n{note.content}")

            note_label.grid(row=(idx + 5), column=0, columnspan=2)


class Note(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        back_button = ttk.Button(
            self,
            text="Back",
            command=lambda: controller.show_frame(Home)
        )

        back_button.grid(row=0, column=0, columnspan=3)

        title_label = ttk.Label(master=self, text="Title")

        title_label.grid(row=1, column=1, columnspan=3)

        title_field = ttk.Entry(master=self)

        title_field.grid(row=1, column=2, columnspan=3)

        note_field = ttk.Entry(master=self)

        note_field.grid(row=2, column=0, columnspan=3)
