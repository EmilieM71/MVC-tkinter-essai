from tkinter import *

class View1:
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()

    def callback(self, event):
        pass

    def create_widgets(self):
        button1 = Button(self.frame, text=" Click me ! ", command=lambda event: print(event))
        button1.pack()
