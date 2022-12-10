## Buttons

import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("MY GUI")

frame = tk.Frame(root, bg="yellow", borderwidth=6)
frame.pack(side='left', fill="y", padx=300)

button = tk.Button(frame, fg='red', text='Click here')
button.pack(side='top')

button2 = tk.Button(frame, fg='red', text='Click here')
button2.pack(side='top', pady=50)




root.mainloop()



