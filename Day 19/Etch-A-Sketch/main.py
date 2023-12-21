from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def backword():
    tim.backward(100)

def counter_clockwise():
    tim.left(90)
    
def clockwise():
    tim.right(90)

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=backword)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)

screen.exitonclick()