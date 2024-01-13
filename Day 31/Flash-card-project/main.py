BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

data = pandas.read_csv("/home/amul/Documents/anjela python/Day 31/Flash-card-project/data/french_words.csv")

current_card = {}

to_learn = data.to_dict(orient="records")

def next_card():
    global current_card
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title,text = "French")
    canvas.itemconfig(card_text,text = current_card["French"])

def flip_card():
    canvas.itemconfig(card_title,text = "English")
    canvas.itemconfig(card_text, text = current_card["English"])
    canvas.itemconfig(card_background,image = card_back_img)


window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("flashy")


window.after(3000,func=flip_card)
canvas = Canvas(width=800,height=526)

card_front_img = PhotoImage(file = "/home/amul/Documents/anjela python/Day 31/Flash-card-project/images/card_front.png")
card_back_img = PhotoImage(file="/home/amul/Documents/anjela python/Day 31/Flash-card-project/images/card_back.png")
card_background = canvas.create_image(400,263,image = card_front_img)
card_title = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
card_text = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image = PhotoImage(file="/home/amul/Documents/anjela python/Day 31/Flash-card-project/images/wrong.png")
unknown_button = Button(image=cross_image,command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="/home/amul/Documents/anjela python/Day 31/Flash-card-project/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1,column=1)

window.mainloop()