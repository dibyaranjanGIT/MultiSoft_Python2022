## Frames in TkInter
## Frame are slices in window, which is defined what we have to include while creating our GUI

import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("MY GUI") # To change the title of your GUI

frame = tk.Frame(root, bg="yellow", borderwidth=6)
frame.pack(side='left', fill="y", padx=20)

frame2 = tk.Frame(root, bg="red", borderwidth=6)
frame2.pack(side='right', fill="y", padx=20)

label = tk.Label(frame, text="My GUI Application")
label.pack()


label2 = tk.Label(frame2, text="My GUI Application")
label2.pack()


root.mainloop()