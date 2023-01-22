# Adding multiple Menus and Submenus
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


file_menu = Menu(menubar, tearoff=0)  # tear off allows you to detach menus for the main window creating floating menus

root.config(menu=menubar)
menubar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Save", command=my_func)
file_menu.add_command(label="Save As", command=my_func1)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit) #### Exit on click

file_menu = Menu(menubar, tearoff=0)  # tear off allows you to detach menus for the main window creating floating menus



## Edit Menu
edit_menu = Menu(menubar, tearoff=0)  # tear off allows you to detach menus for the main window creating floating menus

root.config(menu=menubar)
menubar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut", command=my_func)
edit_menu.add_command(label="Copy", command=my_func1)
edit_menu.add_separator()
edit_menu.add_command(label="Exit", command=root.quit)


root.mainloop()
