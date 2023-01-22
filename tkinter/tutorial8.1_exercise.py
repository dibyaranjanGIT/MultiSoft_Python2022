# Entry Widget and How to create a variable in tkinter

from tkinter import Tk, StringVar, Entry, Button,Label

root = Tk()
root.geometry("600x400")
root.title("MY GUI")

# Variable types in tkinter.
# BooleanVar , DoubleVar, IntVar, StringVar
# *IMP* The variable class has two methods get and set
user_value = StringVar()
password = StringVar()
label1 = Label(text="Username")
label2 = Label(text="Password")
# Entry widget is a widget in which you can enter the value
user_entry = Entry(root, textvariable=user_value)
pass_entry = Entry(root, textvariable=password)
label1.grid(row=0,column=1)
label2.grid(row=1,column=1)
user_entry.grid(row=0, column=2)
pass_entry.grid(row=1, column=2)


def getvals():
    print(user_value.get())
    print(password.get())


button = Button(text='Submit', command=getvals)
button.grid(row=3, column=2)

root.mainloop()
