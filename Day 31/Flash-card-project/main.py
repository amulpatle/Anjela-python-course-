BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("flashy")

canvas = Canvas(width=800,height=526)

card_front_img = PhotoImage(file = "/home/amul/Documents/anjela python/Day 31/Flash-card-project/images/card_front.png")
canvas.create_image(400,263,image = card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0)




window.mainloop()