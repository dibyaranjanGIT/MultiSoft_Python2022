## Menus and Submenus
from tkinter import Tk, Menu

canvas_width = 600
canvas_height = 400

root = Tk()
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("My GUI App")

menubar = Menu(root)

def my_func():
    pass

def my_func1():
    pass

m1 = Menu(menubar, tearoff=0)
m1.add_command(label="Save", command=my_func)
m1.add_command(label="Save As", command=my_func1)
m1.add_separator()
m1.add_command(label="Exit", command=quit)

root.config(menu=menubar)
menubar.add_cascade(label="Menu", menu=m1)

#######################################

m2 = Menu(menubar, tearoff=0)
m2.add_command(label="Save", command=my_func)
m2.add_command(label="Save As", command=my_func1)
m2.add_separator()
m2.add_command(label="Exit", command=quit)

root.config(menu=menubar)
menubar.add_cascade(label="Edit", menu=m2)


root.mainloop()