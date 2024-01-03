from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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

scoreboard = Scoreboard()

while is_game_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()
    
    # detect snake collition with food
    if snake.head.distance(food)  < 15:
        # print("yammy")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # detect collition with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        # is_game_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10 :
            # is_game_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
    

screen.exitonclick()