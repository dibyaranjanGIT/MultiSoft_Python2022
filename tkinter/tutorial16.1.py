#################################
## Adding the list item using a button.

from tkinter import *

root = Tk()
root.geometry("455x223")
root.title("List box widget")

lbx = Listbox(root)
lbx.pack()
# lbx.insert(END, "First Item")
i = 0
def add():
    global i
    lbx.insert(ACTIVE, f"item{str(i)}") # This ACTIVE keyword will insert the item in the next
    i = i+1

button = Button(root, text="Add item", command=add)
button.pack()

root.mainloop()