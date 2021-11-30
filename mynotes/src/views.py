from ui.home_view import Home
from ui.login_view import Login
from ui.create_user import CreateUser
from db.mock_models import init_users
import tkinter as tk

HEIGHT = 600
WIDTH = 400
FONT = ("Arial", 24)


class MyNotesApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        users, notes = init_users()

        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title(" MyNotes ")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # passing data to each frame,
        # while I have a mock db made from python objects
        home_view_instance = init_frame(
            Home,
            users,
            notes
        )
        create_user_instance = init_frame(
            CreateUser,
            users,
            notes
        )
        login_view_instance = init_frame(
            Login,
            users,
            notes
        )
        create_user_instance.reference_frames = {
            "home_view_instance": home_view_instance,
            "login_view_instance": login_view_instance,
        }
        login_view_instance.reference_frames = {
            "home_view_instance": home_view_instance,
            "create_user_instance": create_user_instance
        }
        login_view_instance.reference_functions = {
            "validate_login": validate_login
        }
        create_user_instance.reference_functions = {
            "create_user": create_user
        }

        self.frames = {}
        for F in (
            login_view_instance,
            create_user_instance,
            home_view_instance
        ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(login_view_instance)

    def show_frame(self, cont):
        if cont not in self.frames:
            self.frames[cont] = cont(self.container, self)
        frame = self.frames[cont]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")


def init_frame(frame, users, notes):
    frame.init_data(frame, users, notes)
    return frame


def validate_login(username, users):
    for user in users:
        if user.username == username:
            return True
    return False


def create_user():
    print("hi")


myNotesApp = MyNotesApp()
myNotesApp.mainloop()
