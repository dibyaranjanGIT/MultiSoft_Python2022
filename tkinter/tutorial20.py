# More on tkinter

from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("My GUI")

# How to set up a favicon (icon) for your GUI app
root.wm_iconbitmap("favi.ico")

# How to configure the root window
root.configure(background='grey')

# How to get the screen width and height
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# print(f"{width},{height}")

# Button to close the root window
Button(text="Close", command=root.destroy).pack()

root.mainloop()