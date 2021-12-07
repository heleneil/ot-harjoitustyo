import tkinter as tk
from ui.views import Login, CreateUser, Home, Note
from models.mock_models import User, read_notes_from_file_for_user, read_users_from_file, write_user_to_file

HEIGHT = 600
WIDTH = 400
FONT = ("Arial", 24)


class MyNotesApp(tk.Tk):

    session_user = User('', '')

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
        if container not in self.frames:
            self.frames[container] = container(self.container, self)
        frame = self.frames[container]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")

    def set_session_user(self, user):
        self.session_user = user
        self.init_frames()
        print(f"The session user is now {self.session_user.username}")

    def validate_login(self, username):
        for user in read_users_from_file():
            if user.username == username:
                return user

    def create_user(self, username):
        user_exists = self.validate_login(username)
        if user_exists is not None:
            return "User already exists"
        if len(username) < 3:
            return "Username is too short"

        # if no errors, then
        new_user = write_user_to_file(username)
        self.set_session_user(new_user)

    def get_notes(self):
        return read_notes_from_file_for_user(self.session_user)


def build_my_notes_app():
    myNotesApp = MyNotesApp()
    myNotesApp.mainloop()
