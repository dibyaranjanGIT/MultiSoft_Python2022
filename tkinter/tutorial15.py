## Radio buttons
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x223")
root.title("Radio Button Tutorial")

def order_():
    tmsg.showinfo("Order", f"You ordered {var.get()}")

# var = IntVar()
# var.set(1)
var = StringVar()
var.set("Radio")
label = Label(root, text='What would you like to have sir !', justify=LEFT, padx=14,
              font='lucdia 15')
label.pack()

radio = Radiobutton(root, text="Dosa", padx=30, variable=var, value="Dosa")
radio.pack(anchor='w')

radio = Radiobutton(root, text="Idli", padx=30, variable=var, value="Idli")
radio.pack(anchor='w')

radio = Radiobutton(root, text="Samosa", padx=30, variable=var, value="Samosa")
radio.pack(anchor='w')

radio = Radiobutton(root, text="Paratha", padx=30, variable=var, value="Paratha")
radio.pack(anchor='w')

radio = Radiobutton(root, text="Sabji", padx=30, variable=var, value="Sabji")
radio.pack(anchor='w')


button = Button(text="Order now", padx=30, command=order_)
button.pack()



root.mainloop()