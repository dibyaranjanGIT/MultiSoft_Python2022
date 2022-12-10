import tkinter as tk

root = tk.Tk()
# WidthxHeight
root.geometry("600x400") # This defines the shape of your window
# width, height
root.minsize(300, 150) # Then you can't minimize below this point
# width, height
root.maxsize(800, 600) # Then you can't maximize below this point

label = tk.Label(text="GUI App") # This will create a lable
# but as per the tkinter rule this will not be displayed as we have to pack it to the window.
label.pack()


root.mainloop()