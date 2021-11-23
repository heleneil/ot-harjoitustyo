import tkinter as tk
from tkinter import ttk
# from typing import Text
from ui.login_view import Login

FONT = ("Arial", 24)


class MyNotesApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("600x600")
        self.title(" MyNotes ")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, cont):  # cont = page_name
        if cont not in self.frames:
            self.frames[cont] = cont(self.container, self)
        frame = self.frames[cont]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")


class CreateUser (tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Create user", font=FONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(
            self,
            text="Login",
            command=lambda: controller.show_frame(HomePage)
        )

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(
            self,
            text="extra button",
            command=lambda: controller.show_frame(HomePage)
        )

        button2.grid(row=2, column=1, padx=10, pady=10)


class HomePage (tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="MyNotes", font=FONT)

        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(
            self,
            text="Logout",
            command=lambda: controller.show_frame(Login)
        )

        button1.grid(row=1, column=1, padx=10, pady=10)


app = MyNotesApp()
app.mainloop()
