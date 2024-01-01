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
    time.sleep(0.1)
    for seg_num in range(len(segment) -1, 0, -1):
        new_x = segment[seg_num -1].xcor()
        new_y = segment[seg_num- 1].ycor()
        segment[seg_num].goto(new_x,new_y)
    segment[0].forward(20)

screen.exitonclick()