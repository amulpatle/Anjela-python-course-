from turtle import Turtle, Screen

screen = Screen()


screen.setup(width=500,height=400)
colors = ["blue","orange","yellow","green","red","purple",]
y_positon = [-70,-40,-10,20,50,80]
user_bet = screen.textinput(title="Make a bet", prompt="which turtle will won the match? Make a bet")
print(user_bet)



for ind in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[ind])
    tim.penup()
    tim.goto(x=-230,y = y_positon[ind])

screen.exitonclick()