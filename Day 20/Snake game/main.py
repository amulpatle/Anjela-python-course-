from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


is_game_on = True


snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while is_game_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()
    
    # detect snake collition with food
    if snake.head.distance(food)  < 15:
        # print("yammy")
        food.refresh()
    

screen.exitonclick()