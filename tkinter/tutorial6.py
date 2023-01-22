## Buttons

import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("MY GUI")

frame = tk.Frame(root,  borderwidth=20)
frame.pack(side='left', fill="y", padx=300, pady=100)

button = tk.Button(frame, fg='red', text='Click here')
button.pack(side='top')

button2 = tk.Button(fg='red', text='Click here')
button2.pack(side='top', pady=70)


root.mainloop()



