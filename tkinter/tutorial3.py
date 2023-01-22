## How to add image to the tkinter root window

from tkinter import Tk, Label, PhotoImage
from PIL import Image, ImageTk

root = Tk()

root.geometry("800x600")

# To add a photo to the window
photo = PhotoImage(file="funny-face.png")
# Note PhotoImage class only supports png file
label = Label(image=photo)
label.pack()

## To show jpg image we have to make use of the Pillow library from python
# image = Image.open("funny-face.jpg")
# photo = ImageTk.PhotoImage(image=image)
# label = Label(image=photo)
# label.pack()

root.mainloop()
