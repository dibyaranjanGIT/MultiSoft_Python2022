# ## Scroll Bar in Tkinter
# from tkinter import *
#
# root = Tk()
# root.geometry("455x223")
# root.title("Scorll Bar")
#
# # For connecting scrollbar to a widget
# # 1. widget(yscrollcommand = scrollbar.set)
# # 2 scrollbar.config(command=widget.yview)
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
#
# listbox = Listbox(root, yscrollcommand=scrollbar.set)
# for i in range(344):
#      listbox.insert(END, f"Item {i}")
# listbox.pack(fill="both", padx=20)
#
# scrollbar.config(command=listbox.yview)
#
# root.mainloop()

##############################################################

from tkinter import *

# create a root window.
top = Tk()

# create listbox object
listbox = Listbox(top, height = 10,
				width = 15,
				bg = "grey",
				activestyle = 'dotbox',
				font = "Helvetica",
				fg = "yellow")

# Define the size of the window.
top.geometry("300x250")

# Define a label for the list.
label = Label(top, text = " FOOD ITEMS")

# insert elements by their
# index and names.
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")

# pack the widgets
label.pack()
listbox.pack()


# Display until User
# exits themselves.
top.mainloop()
