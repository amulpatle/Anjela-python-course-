from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
colors = ["royal blue","firebrick","violet","purple","red","pink","forest green	","orange"]
direction = [0,90,180,270]
tim.width(7)
for _ in range(200):
    tim.forward(30)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(direction))
    
screen.exitonclick()
screen.exitonclick()