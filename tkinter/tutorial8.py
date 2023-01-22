#Grid layout
import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
root.title("MY GUI")

# Grids are just like pack
# Grids are like excel first cell is (0,0) second cell is (0,1)
# one is row and other is column for that matter.
# *IMP* Until you fill 0,0 cell you can fill the 0,1 cell, same goes for the subsequent cell as well

user_name = tk.Label(root, text="Username")
password = tk.Label(root, text="Password")
password1 = tk.Label(root, text="Password")
button = tk.Button(root, text='Click me')

user_name.grid(row=0, column=1)
password.grid(row=1, column=2)

user_name.grid()
password1.grid(row=5, column=3)
# button.grid(row=2, column=1)

root.mainloop()