## Entry widget and Checkbuttons

import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("MY GUI")

label = tk.Label(text="Welcome to Python Class", font="comicsansms 13 bold", pady=10)
label.grid(row=0, column=3)

name = tk.Label(text="Name")
name.grid(row=1, column=1)

phone = tk.Label(text="Phone")
phone.grid(row=2, column=1)

gender = tk.Label(text="Gender")
gender.grid(row=3, column=1)

# i_agree = tk.Label(text="I agree")
# i_agree.grid(row=4, column=1)

name_value = tk.StringVar()
phone_value = tk.StringVar()
gender_value = tk.StringVar()
agreed_to_admit = tk.BooleanVar()

name_entry = tk.Entry(textvariable=name_value)
phone_entry = tk.Entry(textvariable=phone_value)
gender_entry = tk.Entry(textvariable=gender_value)
agree_check = tk.Checkbutton(text='I agree',textvariable=agreed_to_admit)

name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
agree_check.grid(row=4, column=3)


def get_val():
    print("This is done!")
    print(name_value.get()) 
    with open("detail.txt", mode='w') as file:
        file.write(f"{name_value.get()}\n{phone_value.get()}\n{gender_value.get()}\n{agreed_to_admit.get()}")


submit = tk.Button(text='Submit', padx=10, command=get_val)
submit.grid(row=5, column=3)

root.mainloop()
