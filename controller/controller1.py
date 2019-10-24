from tkinter import *
from model.model1 import Model1
from View.view import View


class Controller:
    def __init__(self):
        self.window = Tk()
        self.model = Model1()
        self.view = View(self.window)

    def start(self):
        self.window.title("Essai 2")

        self.window.mainloop()
