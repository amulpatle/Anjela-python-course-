from tkinter import *

THEME_COLOR = "#375362"

class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("quizila")
        # self.canvas = Canvas()
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.score_label  = Label(text="Score : 0",fg = "white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,150,text="Some Question Text",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row = 1,column = 0, columnspan = 2,pady=50)
        
        true_image = PhotoImage(file="/home/amul/Documents/anjela python/Day 34/Quiz app/images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0)
        self.true_button.grid(row=2,column=0)
        
        false_imagee = PhotoImage(file="/home/amul/Documents/anjela python/Day 34/Quiz app/images/false.png")
        self.false_button = Button(image=false_imagee,highlightthickness=0)
        self.false_button.grid(row=2,column=1)
        
        self.window.mainloop()