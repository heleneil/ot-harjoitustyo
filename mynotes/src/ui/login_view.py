from tkinter import Tk, ttk


class Login:

    def __init__(self, root):
        self._root = root
        self._entry = None

    def start(self):
        title_label = ttk.Label(master=self._root, text="Login")

        username_label = ttk.Label(master=self._root, text="Username")
        username_field = ttk.Entry(master=self._root)

        login_button = ttk.Button(master=self._root, text="Log In")

        title_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        username_field.grid(row=1, column=1)

        login_button.grid(row=2, column=0, columnspan=2)

        create_user_button = ttk.Button(master=self._root, text="Create user")

        create_user_button.grid(row=3, column=0, columnspan=2)


window = Tk()
window.title("MyNotes")

login = Login(window)
login.start()

window.mainloop()
