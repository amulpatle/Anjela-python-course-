from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")


# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# screen = Screen()
# screen.exitonclick()
for _ in range (20):
    timmy.forward(10)
    # timmy.delay(50)     
    timmy.pd()
    timmy.forward(10)
    timmy.penup()
    
screen = Screen()
screen.exitonclick()
