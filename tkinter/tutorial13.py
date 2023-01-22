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


file_menu = Menu(menubar, tearoff=0)  # tear off allows you to detach menus for the main window creating floating menus

root.config(menu=menubar)
menubar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Save", command=my_func) # To add_command is to add functionality to our menu
file_menu.add_command(label="Exit", command=quit)
'''
To display the menu in root we have to use Config and Cascade just like Pack and Grid

Config can be used in other widgets as well like Lable, 
Button and it it used to update the things in real time
'''


root.mainloop()
