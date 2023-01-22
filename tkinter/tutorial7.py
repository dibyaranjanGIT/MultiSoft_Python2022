## How to add functionaltiy to button
## This can be done by passing the function name to the command parameter of a button

import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
root.title("MY GUI")

def hello():
    print("Hello Jeeban")




# frame1 = tk.Frame(root, bg="green", borderwidth=6)
# frame1.pack(side='left', fill="y", padx=150)

button = tk.Button( fg='red', text='Click here', command=hello)
button.pack(anchor='c',pady=100)

# label = tk.Label(frame1, text="Hello")
# label.pack()


root.mainloop()



