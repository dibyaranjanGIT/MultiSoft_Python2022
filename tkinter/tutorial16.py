# How to creat Listbox widget using tkinter.
"""
The Listbox() widget is a standard Tkinter widget that displays a list of items from which a user can select a number of
items.
The Listbox can only contain text items, and all items must have the same font and color. Depending on the widget
configuration, the user can choose one or more alternatives from the list.
"""

from tkinter import *

# create a root window.
root = Tk()
root.geometry("600x350")

# create listbox object
listbox = Listbox(root, height=10, width=15, bg="white", font="Helvetica", fg="blue")

# Define a label for the list.
label = Label(root, text=" FOOD ITEMS")

# insert elements by their
# index and names.
listbox.insert(0, "Samosa")
listbox.insert(1, "Pizza")
listbox.insert(2, "IceCream")

# pack the widgets
label.pack()
listbox.pack()


def select():
    label.config(text=listbox.get(ANCHOR))  # Anchor is to get the item highlighted


button = Button(text='Select', command=select)
button.pack()

label = Label(text='5')
label.pack()

root.mainloop()
