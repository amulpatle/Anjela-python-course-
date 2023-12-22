from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

segment_position = [(0,0),(-20,0),(-40,0)]

segment1 = Turtle(shape="square")
segment1.color("white")

for position in segment_position:
    segment1 = Turtle(shape="square")
    segment1.color("white")
    segment1.goto(position)

screen.exitonclick()