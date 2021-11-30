import tkinter as tk
from ui.home_view import Home
from ui.login_view import Login
from ui.create_user import CreateUser
from models.mock_models import read_users_from_file

HEIGHT = 600
WIDTH = 400
FONT = ("Arial", 24)


class MyNotesApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title(" MyNotes ")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        home_view_instance = Home
        create_user_instance = CreateUser
        login_view_instance = Login

        # passing data to each frame,
        # while I have a mock db made from python objects
        load_frame_data(
            home_view_instance,
            reference_frames={},
            reference_functions={}
        )
        load_frame_data(
            create_user_instance,
            reference_frames={
                "home_view_instance": home_view_instance,
                "login_view_instance": login_view_instance,
            },
            reference_functions={
                "create_user": create_user
            }
        )
        load_frame_data(
            login_view_instance,
            reference_frames={
                "home_view_instance": home_view_instance,
                "create_user_instance": create_user_instance
            },
            reference_functions={
                "validate_login": validate_login
            }
        )

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


def load_frame_data(
        frame, reference_frames, reference_functions):
    frame.init_data(frame, reference_frames, reference_functions)


def validate_login(username):
    for user in read_users_from_file():
        if user.username == username:
            return True
    return False


def create_user(username):
    user_exists = validate_login(username)
    if user_exists is False:
        # new_user = create_new_user(username)
        # TODO: write to file
        return True
    return False


def build_my_notes_app():
    myNotesApp = MyNotesApp()
    myNotesApp.mainloop()
