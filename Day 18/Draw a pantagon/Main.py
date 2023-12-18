from turtle import Turtle, Screen
import random
screen = Screen()
tim = Turtle()

colors = ["royal blue","firebrick","violet","purple","red","pink","forest green	","orange"]

def drawShap(newSides):
    angle = 360/newSides
    for _ in range (newSides):
        tim.forward(100)
        tim.right(angle)

for shape_sides in range(3,11):
    tim.color(random.choice(colors))
    drawShap(shape_sides)

screen.exitonclick()
