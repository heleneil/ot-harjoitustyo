import tkinter as tk
from tkinter import ttk
from tkinter import Text

from models.models import Note as NoteObject, delete_note_from_file


class Login(tk.Frame):

    """This class contains the elements of the login frame

    """
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        title_label = ttk.Label(master=self, text="Log in")

        username_label = ttk.Label(master=self, text="Username")
        username_field = ttk.Entry(master=self)

        login_button = ttk.Button(
            self,
            text="Log In",
            command=lambda: self._validate_and_switch_pages(
                controller,
                username_field.get()
                )
        )

        title_label.grid(row=0, column=2, columnspan=3)

        username_label.grid(row=2, column=0)
        username_field.grid(row=2, column=3)

        login_button.grid(row=4, column=2, columnspan=3)

        create_user_button = ttk.Button(
            self,
            text="Create user",
            command=lambda: controller.show_frame(CreateUser)
        )

        create_user_button.grid(row=5, column=2, columnspan=3)

    def _validate_and_switch_pages(self, controller, username):
        validated_user = controller.validate_login(username)
        if validated_user is not None:
            controller.set_session_user(validated_user)
            controller.show_frame(Home)
        else:
            invalid_username_label = ttk.Label(
                master=self, text="Invalid username", foreground='red')
            invalid_username_label.grid(row=2, column=0, columnspan=2)


class CreateUser(tk.Frame):

    """This class contains the elements of the create user frame

    """
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        title_label = ttk.Label(master=self, text="Create user")
        title_label.grid(row=0, column=0, columnspan=2)

        username_label = ttk.Label(master=self, text="Username:")

        username_label.grid(row=2, column=1, columnspan=4)

        username_field = ttk.Entry(master=self)
        username_field.grid(row=2, column=3, columnspan=4)

        username_error_label = None

        create_button = ttk.Button(
            self,
            text="Create and sign in",
            command=lambda: self._create_user_and_switch_page(
                controller,
                username_field.get(),
                username_error_label,
            )
        )

        create_button.grid(row=4, column=0, columnspan=2)

    def _create_user_and_switch_page(
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

    """This class contains the elements of the home frame

    """
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        title_label = ttk.Label(
            master=self,
            text=f"MyNotes\nHello {controller.session_user.username}")

        title_label.grid(row=0, column=2, columnspan=4)

        create_note_button = ttk.Button(
            self,
            text="New note",
            command=lambda: self.set_session_note_and_switch_page(
                controller,
                NoteObject(None, None, None, None)
                )
        )

        create_note_button.grid(row=3, column=2, columnspan=4)

        for idx, note in enumerate(controller.get_notes()):
            note_title_button = ttk.Button(
                master=self,
                text=f"{note.title}",
                command=lambda note=note: self.set_session_note_and_switch_page(
                    controller,
                    note
                    )
                )

            note_title_button.grid(row=(idx + 5), column=2, columnspan=4)

    def set_session_note_and_switch_page(self, controller, note):
        controller.set_session_note(note)
        controller.show_frame(Note)


class Note(tk.Frame):

    """This class contains the elements of the individual note frame

    """
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        back_button = ttk.Button(
            self,
            text="Back",
            command=lambda: controller.show_frame(Home)
        )

        back_button.grid(row=0, column=1, columnspan=3)

        save_button = ttk.Button(
            self,
            text="Save",
            command=lambda: self.create_note_and_switch_page(
                controller,
                title_field.get(),
                note_field.get("1.0", "end-1c")
            )
        )

        save_button.grid(row=0, column=2)

        delete_button = ttk.Button(
            self,
            text='Delete',
            command=lambda: self.delete_note_and_switch_page(
                controller
            )
        )

        if controller.session_note.title is not None:
            delete_button.grid(row=5, column=1, columnspan=3)

        title_label = ttk.Label(master=self, text="Title")

        title_label.grid(row=1, column=0)

        title_field = ttk.Entry(
            master=self,
            )

        title_field.grid(row=1, column=1)

        note_field = Text(
            self,
            height=20,
            width=40,
            )

        note_field.grid(row=2, column=1)

        if controller.session_note.title is not None and controller.session_note.content is not None:
            set_text(title_field, controller.session_note.title, 0)
            set_text(note_field, controller.session_note.content, 1.0)

    def create_note_and_switch_page(
        self,
        controller,
        title,
        content
    ):
        # replace all the "enter" chars with something
        content = content.replace("\n", " ")

        note = controller.session_note
        note.title = title
        note.content = content
        note.user_id = controller.session_user.id

        controller.create_or_update_note(note)
        controller.show_frame(Home)

    def delete_note_and_switch_page(
        self,
        controller
    ):
        note = controller.session_note
        delete_note_from_file(note)
        controller.set_session_note(NoteObject(None, None, None, None))
        controller.set_notes(controller.get_notes().remove(note))
        controller.show_frame(Home)


def set_text(entry, text, entry_index):
    entry.delete(entry_index, tk.END)
    entry.insert(entry_index, text)
