from tkinter import Tk, ttk

class CreateUser:

    def __init__(self, root):
        self._root = root
        self._entry = None

    def start(self):
        title_label = ttk.Label(master=self._root, text="Create user")
        title_label.grid(row=0, column=0, columnspan=2)

        name_label = ttk.Label(master=self._root, text="Name:")
        username_label = ttk.Label(master=self._root, text="Username:")

        name_label.grid(row=1, column=1)
        username_label.grid(row=2, column=1)

        name_field = ttk.Entry(master=self._root)
        username_field = ttk.Entry(master=self._root)

        name_field.grid(row=1, column=2)
        username_field.grid(row=2, column=2)


window = Tk()
window.title("MyNotes")

create_user = CreateUser(window)
create_user.start()

window.mainloop()
