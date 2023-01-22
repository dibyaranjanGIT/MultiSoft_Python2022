import tkinter as tk

root = tk.Tk()
root.geometry('200x300')

height_value = tk.IntVar()
width_value = tk.IntVar()

def change_geometry():
    root.geometry(f"{height_value.get()}x{width_value.get()}")

label1 = tk.Label(text='Height ')
label1.grid(row=0, column=0)
height_ent = tk.Entry(root,textvariable=height_value)
height_ent.grid(row=0, column=1)

label1 = tk.Label(text='Width ')
label1.grid(row=1,column=0)
height_ent = tk.Entry(root, textvariable=width_value)
height_ent.grid(row=1,column=1)


button1 = tk.Button(root,text="submit", command=change_geometry)
button1.grid(row=2, column=1)

root.mainloop()