########################################################################
#Date: 23.02.22                                                        #
#Programmed by: Luka Henig (luka.henig@gmail.com)                      #
#Curse: 100 Days of Code(udemy)                                        #
#Description:A simple Pomodoro timer to learn and understand python    #
#and building GUI with Tkinter                                         #
########################################################################
# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
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
MIN_TO_SEC = 60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_lbl.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    stage_lbl.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * MIN_TO_SEC
    short_break_sec = SHORT_BREAK_MIN * MIN_TO_SEC
    long_break_sec = LONG_BREAK_MIN * MIN_TO_SEC

    if(reps % 8 == 0):
        count_down(long_break_sec)
        timer_lbl.config(text="Break", fg=RED)
    elif(reps % 2 == 1):
        count_down(work_sec)
        timer_lbl.config(text="Work", fg=GREEN)
    elif(reps % 2 == 0):
        count_down(short_break_sec)
        timer_lbl.config(text="Break", fg=PINK)
    else:
        print("An timing error corrupted")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if(count > 0):
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "🗸"
        stage_lbl.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
#window configuration
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

#background and timer configuration
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="src/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

#buttons and label configuaration
start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

timer_lbl = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_lbl.grid(row=0, column=1)

stage_lbl = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 24, "bold"))
stage_lbl.grid(row=3, column=1)

#to keep screen alive
window.mainloop()