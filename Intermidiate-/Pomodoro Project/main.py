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
CHECK_MARK = "✓"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer")
    check_label.config(text = "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if (reps % 8 == 0):
        title_label.config(text = "Break", fg = RED)
        count_down(LONG_BREAK_MIN * 60)
    
    elif (reps % 2 == 1):
        title_label.config(text = "Work", fg = GREEN)
        count_down(WORK_MIN * 60)
    elif (reps % 2 == 0):
        title_label.config(text = "Break", fg = PINK)
        count_down(SHORT_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    if min_count < 10:
        min_count = f"0{min_count}"
    
    canvas.itemconfig(timer_text, text = f"{min_count}:{sec_count}")
    if (count > 0):
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += CHECK_MARK
        check_label.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100,130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)

title_label = Label(text = "Timer", fg = GREEN, font = (FONT_NAME, 35, "bold"), bg = YELLOW)
title_label.grid(row = 0, column = 1)

start_button = Button(text = "Start", highlightthickness = 0, command = start_timer)
start_button.grid(row = 2, column = 0)

reset_button = Button(text = "Reset", highlightthickness = 0, command = reset_timer)
reset_button.grid(row = 2, column = 2)

check_label = Label(text = CHECK_MARK, fg = GREEN, font = (FONT_NAME, 20, "bold"), bg = YELLOW)
check_label.grid(row = 3, column = 1)




window.mainloop()