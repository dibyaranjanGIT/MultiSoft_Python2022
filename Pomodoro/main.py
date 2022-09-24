import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = math.floor(count%60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_lable= tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_lable.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)

image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 115, image=image)
timer_text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

start_button = tkinter.Button(text='Reset', highlightthickness=0)
start_button.grid(column=2, row=2)


window.mainloop()