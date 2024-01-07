from tkinter import *
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
    count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    canvas.itemconfigure(timer_text,text = count)
    if count > 0:
        window.after(1000,count_down,count-1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg = YELLOW)

timer_label = Label(text="Timer",fg=GREEN,bg=YELLOW, font=(FONT_NAME,33,"bold"))
# timer_label.size(50,20)
timer_label.grid(column=1,row=0)

canvas = Canvas(width=200,height=224,bg = YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="/home/amul/Documents/anjela python/Day 28/tomato.png")
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


start_button = Button(text="start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="reset", highlightthickness=0)
reset_button.grid(column=2,row=2)

check_mark = Label(text="✔️", fg=GREEN,bg = YELLOW, )
check_mark.grid(column=1,row=3)

window.mainloop()