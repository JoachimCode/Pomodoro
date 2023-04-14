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
window = tkinter.Tk()
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    global reps
    print(reps)
    reps += 1
    work_seconds = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if reps == 9:
        timer_label.config(text="Done")
        countdown(0)
    if reps == 8:
        timer_label.config(text="Break", fg=RED)
        countdown(long_break)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break)
    elif reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_seconds)


def countdown(count):
    checkmarks = ""
    global reps
    global my_timer
    seconds = count%60
    minutes = round((count-seconds)/60)
    if seconds < 10:
        seconds = f"0{seconds}"
#    if seconds > 10 and minutes > 10:
#        canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
#    elif seconds < 10 and minutes < 10:
#        canvas.itemconfig(timer_text, text=f"0{minutes}:0{seconds}")
#    elif seconds > 10 and minutes < 10:
#        canvas.itemconfig(timer_text, text=f"0{minutes}:{seconds}")
#    elif seconds < 10 and minutes > 10:
#        canvas.itemconfig(timer_text, text=f"{minutes}:0{seconds}")
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > -1:
        my_timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        for n in range(math.floor(reps/2)):
            checkmarks += "✔"
        checkmark_label.config(text=checkmarks)

# ---------------------------- UI SETUP ------------------------------- #

window.minsize(720, 500)
window.title("Pomodoro timer")
window.config(pady=100, padx=240, bg=YELLOW)



tomato_img = tkinter.PhotoImage(file="tomato.png")

canvas = tkinter.Canvas()
canvas.config(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="White")
canvas.grid(column=1, row=1)

timer_label = tkinter.Label()
timer_label.config(text="Timer", font = (FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = tkinter.Button()
start_button.config(text="Start", font=20, width=6, command=start_timer)
start_button.grid(column=0, row=2, pady=30, padx=10)

reset_button = tkinter.Button()
reset_button.config(text="Reset", font=20, command=reset)
reset_button.grid(column=2, row=2, pady=30, padx=10,)

checkmark_label = tkinter.Label()
checkmark_label.config(text="", font=80, bg=YELLOW, fg=GREEN)
checkmark_label.grid(column=1, row=3, )








window.mainloop()