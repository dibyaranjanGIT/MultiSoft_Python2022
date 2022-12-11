## Canvas widget creation with Events
## Events are nothing but the action that are created by the user

import tkinter as tk

root = tk.Tk()

canvas_width = 600
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("MY GUI")


# This will give an error, because we haven't passed any event as an argument here
# def display_text():
#     pass

# Define a function to display the message
def display_text(e):
    print("You clicked on the button")


widget = tk.Button(root, text='Click here')
widget.pack()

widget.bind('<Button-1>', display_text)

root.mainloop()
