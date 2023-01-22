import tkinter as tk

root = tk.Tk()
root.geometry('800x600')

frame1 = tk.Frame(root,borderwidth=2,bg='gray')
frame1.pack(anchor='w',padx=100, pady=130)

button1 = tk.Button(frame1,fg='red',bd=3,relief='solid', text="7", padx=16, pady=10)
button1.grid(row=0,column=2)

button1 = tk.Button(frame1,fg='red',bd=3,relief='solid',text="2",padx=16,pady=10)
button1.grid(row=2,column=1)
button1 = tk.Button(frame1,fg='red',bd=3,relief='solid',text="3",padx=16,pady=10)
button1.grid(row=2,column=2)
button1 = tk.Button(frame1,fg='red',bd=3,relief='solid',text="4",padx=16,pady=10)
button1.grid(row=1,column=0)
button1 = tk.Button(frame1,fg='red',bd=3,relief='solid',text="5",padx=16,pady=10)
button1.grid(row=1,column=1)
button1 = tk.Button(frame1,fg='red',bd=3,relief='solid',text="6",padx=16,pady=10)
button1.grid(row=1,column=2)
button1 = tk.Button(frame1,fg='red',bd=3,relief='solid',text="1",padx=16,pady=10)
button1.grid(row=2,column=0)
button1 = tk.Button(frame1,fg='red',bd=3,relief='solid',text="8",padx=16,pady=10)
button1.grid(row=0,column=1)
button1 = tk.Button(frame1,fg='red',bd=3,relief='solid',text="9",padx=16,pady=10)
button1.grid(row=0,column=0)

button1 = tk.Button(frame1,fg='red',bd=3,relief='solid',text="0",padx=16,pady=10)
button1.grid(row=3,column=0)
button1 = tk.Button(frame1,fg='red',bd=3,relief='solid',text=". ",padx=16,pady=10)
button1.grid(row=3,column=1)
button1 = tk.Button(frame1,fg='red',bd=3,relief='solid',text="=",padx=16,pady=10)
button1.grid(row=3,column=2)

root.mainloop()