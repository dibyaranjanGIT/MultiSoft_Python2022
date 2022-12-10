import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.geometry("800x600")

# # To add a photo to the window
# photo = tk.PhotoImage(file="funny-face.png") # it only support png
# label = tk.Label(image=photo)
# label.pack()

# To show jpg image we have to make use of the Pillow library from python
image = Image.open("funny-face.jpg")
photo = ImageTk.PhotoImage(image=image)
label = tk.Label(image=photo)
label.pack()

root.mainloop()