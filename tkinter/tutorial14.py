## Creating sliders in tkinter
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x223")
root.title("MY GUI")


# slider = Scale(root, from_=0, to=400)
# slider.pack()

def getdollar():
    # print(f"You got {slider.get()} from this app")
    tmsg.showinfo("Amount Credit", f"You got {slider.get()}$ from us")


# To create a slider in the horizontal direction
slider = Scale(root, from_=0, to=100, length=250, orient=HORIZONTAL, tickinterval=25)
button = Button(root, text='Get dollars', command=getdollar)
slider.pack()
button.pack()

root.mainloop()
