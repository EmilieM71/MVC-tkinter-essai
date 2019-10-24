from tkinter import *
from View.view1 import View1


class View:
    def __init__(self, root):
        self.frame_view1 = Frame(root)
        self.frame_view1.pack()
        self.view1 = View1(self.frame_view1)
