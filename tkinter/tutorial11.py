# Canvas widget creation with Events
# Events are nothing but the action that are created by the user

import tkinter as tk

root = tk.Tk()

canvas_width = 600
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("MY GUI")


# Define a function to display the message
# here e is the event that we passed in.
def display_text(e):
    print("You clicked on the button")


button = tk.Button(root, text='Click here')
button.pack()

button.bind('<Button-3>', display_text)
# bind takes two things one is event and other is action
'''

list of all events in tkinter
https://www.tutorialspoint.com/list-of-all-tkinter-events
'''


root.mainloop()
