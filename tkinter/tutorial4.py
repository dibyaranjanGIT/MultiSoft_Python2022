## How to set properties of Widgets
import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("MY GUI")

## Widgets properties
# text/image = add the text/ add image
# bg = background
# fg = foreground
# font = sets the font
# padx = x padding
# pady = y padding
# relief = border styling - SUNKEN, RAISED, GROOVE, RIDGE

# lable = tk.Label(text="This is a demo GUI app")
# lable.pack()

# lable = tk.Label(text="This is a demo GUI app", bg='green', fg='blue')
# lable.pack()

# lable = tk.Label(text="This is a demo GUI app", bg='red', fg='blue', padx=23, pady=20)
# lable.pack()

# lable = tk.Label(text="This is a demo GUI app", bg='grey', fg='red', padx=23, pady=20,
#                  font=("Comic Sans MS", 30, "bold"))
# lable.pack()

## or you can pass the font as a string
# lable = tk.Label(text="This is a demo GUI app", bg='grey', fg='red', padx=23, pady=20,
#                  font="'comicsanms 19 bold")
# lable.pack()

## Border styling
# lable = tk.Label(text="This is a demo GUI app", bg='red', fg='blue', padx=23, pady=20,
#                  font="comicsanms 19 bold", relief=tk.GROOVE)
# lable.pack()

# ## Postion of the lable
lable = tk.Label(text="This is a demo GUI app", bg='red', fg='blue', padx=23, pady=20,
                 font="comicsanms 19 bold", relief="groove")
lable.pack(anchor='c') # nw means north west


'''
side − Determines which side of the parent widget packs against: 
TOP (default), BOTTOM, LEFT, or RIGHT.
'''
# lable = tk.Label(text="This is a demo GUI app", bg='red', fg='blue', padx=23, pady=20,
#                  font="comicsanms 19 bold")
# lable.pack(anchor='c', side="bottom")

## Fill is to fill the entire length of the window
# lable = tk.Label(text="This is a demo GUI app", bg='red', fg='blue', padx=23, pady=20,
#                  font="comicsanms 19 bold")
# lable.pack(anchor='nw', fill='x')
# lable.pack(anchor='sw', side="bottom", fill='x')



root.mainloop()

## How anchow works
"""
|-------------------|
|                   |
| NW     N      NE  |
|                   |
| W      C       E  |
|                   |
| SW     S      SE  |
|                   |
|-------------------|
"""
