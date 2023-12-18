from turtle import Turtle, Screen
import random

direction = []

tim = Turtle
screen = Screen()

angle = [1,90,180]

for i in range(20):
    tim.forward(random.choice(360/angle))
    
# screen.mainloop()