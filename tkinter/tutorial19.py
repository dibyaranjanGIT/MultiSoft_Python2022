## Using Classes and Objects
from tkinter import *


class GUI(Tk):
    def __init__(self): # here self = root
        super().__init__()
        self.geometry("600x500")

    def status_bar(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.staus_ = Label(self, textvar=self.var, relief=SUNKEN, anchor=W)
        self.staus_.pack(side=BOTTOM, fill=X)

    def click(self):
        pass

    def create_button(self):
        self.button = Button(text="Click Me", command=self.click).pack()

if __name__ == "__main__":
    window = GUI()
    window.status_bar()
    window.create_button()
    window.mainloop()