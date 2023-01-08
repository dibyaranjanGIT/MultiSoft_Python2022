# How to creat Listbox widget using tkinter.
"""
The Listbox() widget is a standard Tkinter widget that displays a list of items from which a user can select a number of
 items. The Listbox can only contain text items, and all items must have the same font and color. Depending on the widget configuration, the user can choose one or more alternatives from the list.
"""

from tkinter import *

# create a root window.
root = Tk()
root.geometry("600x350")

# create listbox object
listbox = Listbox(root, height = 10, width = 15, bg = "grey", font = "Helvetica", fg = "yellow")

# Define a label for the list.
label = Label(root, text = " FOOD ITEMS")

# insert elements by their
# index and names.
listbox.insert(1, "Samosa")
listbox.insert(2, "Dahibara")
listbox.insert(3, "Aloochop")
listbox.insert(4, "Pizza")
listbox.insert(5, "IceCream")

# pack the widgets
label.pack()
listbox.pack()


# Display until User
# exits themselves.
root.mainloop()





