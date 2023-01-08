## How to create message box

## Radio buttons
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x223")
root.title("Radio Button Tutorial")

def show_message():
    tmsg.showinfo("Message", "This is a message from tkinter")


label = Label(root, text='Click on the below button', justify=LEFT, padx=14,
              font='lucdia 10')
label.pack()

button = Button(text="Show message", padx=30, command=show_message)
button.pack()

root.mainloop()


"""
Types of message box 
-------------------
messagebox.showinfo("showinfo", "Information")
messagebox.showwarning("showwarning", "Warning")
messagebox.showerror("showerror", "Error")
messagebox.askquestion("askquestion", "Are you sure?")
messagebox.askokcancel("askokcancel", "Want to continue?")
messagebox.askyesno("askyesno", "Find the value?")
messagebox.askretrycancel("askretrycancel", "Try again?")  

"""