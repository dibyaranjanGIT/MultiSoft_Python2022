'''
Create an application which will width and hight as
Entry input from the user and resize the root window accordingly
'''


from tkinter import *


root = Tk()
root.geometry("600x400")

def update():
    root.geometry(f"{width.get()}x{height.get()}")

width = StringVar()
height = StringVar()

input1 = Entry(root, textvariable=width)
input1.pack(pady=20)
input2 = Entry(root, textvariable=height)
input2.pack()
button = Button(root, text='Apply', command=update)
button.pack(pady=10)

root.mainloop()