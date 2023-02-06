## Getting the value of a button after pressing it.

from tkinter import *
from tkinter.ttk import *


root = Tk()

# Set the size of the window
root.geometry("300x350")


def on_click(text):
    print(int(text))


frame = Frame(root)
frame.pack(pady=10)

# Add Buttons in the window
b1 = Button(frame, text="1", command=lambda: on_click("1"))
b1.pack(pady=10)

b2 = Button(frame, text="2", command=lambda: on_click("2"))
b2.pack(pady=10)

b3 = Button(frame, text="3", command=lambda: on_click("3"))
b3.pack(pady=10)


root.mainloop()
