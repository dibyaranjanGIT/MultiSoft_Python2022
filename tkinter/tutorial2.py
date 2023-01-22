# Properties associated with root window
import tkinter as tk

root = tk.Tk()

# WidthxHeight
root.geometry("600x400")  # This defines the shape of your window
# width, height
root.minsize(300, 150)  # Then you can't minimize below this point
# width, height
root.maxsize(800, 600)  # Then you can't maximize below this point

# To change the title of your GUI
root.title("MY GUI")

root.mainloop()
