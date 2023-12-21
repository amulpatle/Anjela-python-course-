from turtle import Turtle, Screen

tim = Turtle(shape="turtle")
screen = Screen()


screen.setup(width=500,height=400)

user_bet = screen.textinput(title="Make a bet", prompt="which turtle will won the match? Make a bet")
print(user_bet)

tim.penup()
tim.goto(x=-230,y = -100)

screen.exitonclick()