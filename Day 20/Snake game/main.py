from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

segment_position = [(0,0),(-20,0),(-40,0)]
# segment1 = Turtle(shape="square")
# segment1.color("white")

is_game_on = True

segment = []

for position in segment_position:
    segment1 = Turtle(shape="square")
    segment1.color("white")
    segment1.penup()
    segment1.goto(position)
    segment.append(segment1)

# screen.update()

while is_game_on:
    screen.update()
    for seg in segment:
        seg.forward(20)
        time.sleep(0.1)

screen.exitonclick()