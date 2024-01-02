from turtle import Screen
from turtle import Turtle
from paddle import Paddle
from ball import Ball


screen = Screen()
paddle = Turtle()
ball = Ball()
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

# pong game screen setup
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

is_game_on = True

while is_game_on:
    screen.update()

screen.exitonclick()