## Creating Progress bar
#
# from tkinter import *
# import time
#
# root = Tk()
# root.geometry("455x223")
# root.title("Status Bar")
#
# status_var = StringVar()
# status_var.set("I am status")
#
# sbar = Label(root, textvariable=status_var, relief=SUNKEN)
# sbar.pack(side=BOTTOM, fill=X)
#
# def update_status():
#     sbar.update()
#     status_var.set("Busy..")
#     time.sleep(2)
#     status_var.set("Ready..")
#
# Button(root, text="Upload", command=update_status).pack()
#
# root.mainloop()


# importing tkinter module
from tkinter import *
from tkinter.ttk import Progressbar

# creating tkinter window
root = Tk()
root.geometry('500x250')

# Progress bar widget
progress = Progressbar(root, orient=HORIZONTAL,
                       length=100, mode='determinate')


# Function responsible for the updation
# of the progress bar value
def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100


progress.pack(pady=10)

# This button will initialize
# the progress bar
Button(root, text='Start', command=bar).pack(pady=10)

# infinite loop
mainloop()
