from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
screen.setup(width=500,height=400)
colors = ["blue","orange","yellow","green","red","purple",]
y_positon = [-70,-40,-10,20,50,80]
user_bet = screen.textinput(title="Make a bet", prompt="which turtle will won the match? Make a bet")
print(user_bet)

all_turtle = []

for ind in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[ind])
    tim.penup()
    tim.goto(x=-230,y = y_positon[ind])
    all_turtle.append(tim)
    

if user_bet :
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_Color = turtle.pencolor()
            if winner_Color == user_bet:
                print(f"You have won! The {winner_Color} turtle is winner")
            else:
                print(f"you have lost , The {winner_Color} turtle is winner")
        random_dist =   random.randint(0,10)
        turtle.forward(random_dist)
      


screen.exitonclick()