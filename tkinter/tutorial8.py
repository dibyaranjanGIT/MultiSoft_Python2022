## Entry widget and Grid layout
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
root.title("MY GUI")

## Grids are just like pack
## Grids are like excel first cell is (0,0) second cell is (0,1)
## one is row and other is column for that matter.

user_name = tk.Label(root, text="Username")
password = tk.Label(root, text="Password")
button = tk.Button(root, text='Click me')

user_name.grid()
password.grid(row=1)

# button.grid(row=2, column=1)

root.mainloop()