## Scroll Bar in Tkinter
from tkinter import *

root = Tk()
root.geometry("455x223")
root.title("Scorll Bar")

# For connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command=widget.yview)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(344):
     listbox.insert(END, f"Item {i}")
listbox.pack(fill="both", padx=20)

scrollbar.config(command=listbox.yview)

root.mainloop()
