## Creating status bar

from tkinter import *
import time

root = Tk()
root.geometry("455x223")
root.title("Status Bar")

status_var = StringVar()
status_var.set("I am status")

sbar = Label(root, textvariable=status_var, relief=SUNKEN)
sbar.pack(side=BOTTOM, fill=X)

def update_status():
    status_var.set("Busy..")
    sbar.update() # This update function will take the Busy.. else it will igonre it and  print the last set option
    time.sleep(2)
    status_var.set("Ready..")

Button(root, text="Upload", command=update_status).pack()

root.mainloop()