## Entry widget and Grid layout
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
root.title("MY GUI")

## Grids are just like excel first cell is (0,0) second cell is (0,1)
## one is row and other is column for that matter.
user_name = tk.Label(root, text="Username")
password = tk.Label(root, text="Password")

user_name.grid()
password.grid(row=1)

## Variable types in tkinter.
## BooleanVar , DoubleVar, IntVar, StringVar
## ** Imp ** The variable class has two methods get and set
user_value = tk.StringVar()
password = tk.StringVar()


# Entry widget is a widget in which you can enter the value
user_entry = tk.Entry(root, textvariable=user_value)
pass_entry = tk.Entry(root, textvariable=password)

user_entry.grid(row=0, column=1)
pass_entry.grid(row=1, column=1)

def getvals():
    print(user_value.get())
    print(password.get())

button = tk.Button(text='Submit', command=getvals)
button.grid(row=3, column=1)

root.mainloop()