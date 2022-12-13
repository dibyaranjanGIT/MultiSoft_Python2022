## Menus and Submenus
from tkinter import Tk, Menu

canvas_width = 600
canvas_height = 400

root = Tk()
root.geometry(f"{canvas_width}x{canvas_height}")

root.title("My GUI App")

def open_file():
    pass

def my_func():
    pass

menu = Menu(root)
menu.add_command(label="File", command=open_file)
menu.add_command(label="Save", command=my_func)
menu.add_command(label="Exit", command=quit)


root.config(menu=menu)


root.mainloop()