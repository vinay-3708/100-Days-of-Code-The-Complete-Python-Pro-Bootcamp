from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.2
REPS = 0
TICK_MARK_ROW = 3
TICK_LIST = []
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global REPS, TICK_MARK_ROW, TICK_LIST
    REPS = 0
    TICK_MARK_ROW = 3
    window.after_cancel(timer)
    canvas.itemconfig(tagOrId=timer_text, text="00:00")
    my_label.config(text="Timer")
    for i in TICK_LIST:
        i.grid_remove()
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def tick_mark():
    global TICK_MARK_ROW, TICK_LIST
    tick_label = Label(text="✔", highlightthickness=0, bg=YELLOW, fg=GREEN, font=(FONT_NAME, "10", "bold"))
    tick_label.grid(row=TICK_MARK_ROW, column=1, padx=50, pady=2)
    TICK_LIST.append(tick_label)
    TICK_MARK_ROW += 1


def count_down(count):
    global timer
    min = int(count//60)
    sec = int(count%60)
    if len(str(sec)) == 1:
        sec = "0" + str(sec)
    canvas.itemconfig(tagOrId=timer_text, text=f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if (REPS-1)%2 == 0:
            tick_mark() 

def start_timer():
    global REPS
    REPS += 1
    short_break_sec =  60 * SHORT_BREAK_MIN
    long_break_sec = 60 * LONG_BREAK_MIN
    work_sec = 60 * WORK_MIN
    if REPS%8 == 0:
        my_label.configure(text="Long Break", fg=RED, bg=YELLOW, font=(FONT_NAME, "15", "bold"))
        count_down(long_break_sec)
    elif REPS%2 == 0:
        my_label.configure(text="Short Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, "15", "bold"))
        count_down(short_break_sec)
    else:
        my_label.configure(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, "35", "bold"))
        count_down(work_sec)
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.minsize(width=200, height=224)
window.title("Pamodoro")
window.configure(bg=YELLOW)
bg_image = PhotoImage(file="./Day-28_Tkinter/tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(101, 112, image=bg_image)

my_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, "35", "bold"))
my_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0, padx=50, pady=10)

reset_button = Button(text="Reset", highlightthickness=0, command=timer_reset)
reset_button.grid(row=2, column=2, padx=50, pady=10)


timer_text = canvas.create_text(103, 127, text="00:00", fill="white", font=(FONT_NAME, "35", "bold"))
canvas.grid(row=1,column=1)

# count_down(5)

window.mainloop()