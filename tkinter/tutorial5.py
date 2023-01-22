## Frames in TkInter
## Frame are slices in window, which is defines what we have to include while creating our GUI

from tkinter import Tk, Frame, Label

root = Tk()
root.geometry("800x600")
root.title("MY GUI")  # To change the title of your GUI

frame = Frame(root, bg="yellow", borderwidth=6)
frame.pack(side='left', fill="y", padx=20)

# Here we are creating a Lable inside a frame.
label = Label(frame, text="My GUI Application")
label.pack()

label = Label(text="My GUI Application")
label.pack()


root.mainloop()
