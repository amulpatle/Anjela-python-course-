from turtle import Screen
from turtle import Turtle


screen = Screen()
paddle = Turtle()

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")

paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5,stretch_len=1)
paddle.penup()
paddle.goto(350,0)


screen.exitonclick()