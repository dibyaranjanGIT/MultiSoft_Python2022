## Attributes and Labels
import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("MY GUI") # To change the title of your GUI

## Important lable information
# text = add the text
# bd = background
# fg = foreground
# font = sets the font
# padx = x padding
# pady = y padding
# relief = border styling - SUNKEN, RAISED, GROOVE, RIDGE

# lable = tk.Label(text="This is a demo GUI app", bg='red', fg='blue')
# lable.pack()

# lable = tk.Label(text="This is a demo GUI app", bg='red', fg='blue', padx=23, pady=20)
# lable.pack()

# lable = tk.Label(text="This is a demo GUI app", bg='red', fg='blue', padx=23, pady=20,
#                  font=("comicsanms", 19, "bold"))
# lable.pack()
## or you can pass the font as a string
# lable = tk.Label(text="This is a demo GUI app", bg='red', fg='blue', padx=23, pady=20,
#                  font="comicsanms 19 bold")
# lable.pack()

## Border styling
# lable = tk.Label(text="This is a demo GUI app", bg='red', fg='blue', padx=23, pady=20,
#                  font="comicsanms 19 bold", relief="sunken")
# lable.pack()

# ## Postion of the lable
# lable = tk.Label(text="This is a demo GUI app", bg='red', fg='blue', padx=23, pady=20,
#                  font="comicsanms 19 bold")
# lable.pack(anchor='nw') # nw means north west

# lable = tk.Label(text="This is a demo GUI app", bg='red', fg='blue', padx=23, pady=20,
#                  font="comicsanms 19 bold")
# lable.pack(anchor='nw', side="bottom") # side is bottom

## Fill is to fill the entire length of the window
lable = tk.Label(text="This is a demo GUI app", bg='red', fg='blue', padx=23, pady=20,
                 font="comicsanms 19 bold")
# lable.pack(anchor='nw', side="bottom", fill='x')
lable.pack(anchor='nw', side="bottom", fill='y')



root.mainloop()