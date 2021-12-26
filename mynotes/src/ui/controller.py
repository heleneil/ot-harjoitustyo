import tkinter as tk
from ui.views import Login, CreateUser, Home, Note
from models.models import User, Note as NoteObject, read_notes_from_file_for_user, read_users_from_file, update_note_in_file, write_note_to_file, write_user_to_file

HEIGHT = 600
WIDTH = 400
FONT = ("Arial", 24)


class MyNotesApp(tk.Tk):

    """This class contains the program logic

    """

    session_user = User(None, None)
    session_note = NoteObject(None, None, None, None)
    loaded_notes = []

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title(" MyNotes ")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.init_frames()
        self.show_frame(Login)

    def init_frames(self):
        self.frames = {}
        for F in (
            Home,
            CreateUser,
            Login,
            Note,
        ):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, container):
        """Shows the frame instance for a given generic view class

        Args:
            container: one of the view classes
        """

        if container not in self.frames:
            self.frames[container] = container(self.container, self)
        frame = self.frames[container]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")

    def set_session_user(self, user):
        self.session_user = user
        self.init_frames()

    def validate_login(self, username):
        """Checks the file containing users and makes sure it exists

        Args:
            username: the username that has been entered in the username field
        """

        for user in read_users_from_file():
            if user.username == username:
                return user
        return None

    def create_user(self, username):
        user_exists = self.validate_login(username)
        if user_exists is not None:
            return "User already exists"
        if len(username) < 3:
            return "Username too short"

        # if no errors, then
        new_user = write_user_to_file(username)
        self.set_session_user(new_user)
        return None

    def set_session_note(self, note):
        self.session_note = note
        self.init_frames()

    def create_or_update_note(self, note):
        if note.id:
            self.set_notes(self.get_notes().remove(note))
            note = update_note_in_file(note)
        else:
            note = write_note_to_file(note)

        self.set_notes(self.get_notes().append(note))
        return note

    def get_notes(self):
        if self.loaded_notes is None or len(self.loaded_notes) == 0:
            loaded_notes = read_notes_from_file_for_user(self.session_user)
            self.loaded_notes = loaded_notes
        return self.loaded_notes

    def set_notes(self, notes):
        self.loaded_notes = notes
        self.init_frames()


def build_my_notes_app():
    my_notes_app = MyNotesApp()
    my_notes_app.mainloop()
