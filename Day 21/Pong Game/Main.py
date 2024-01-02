from turtle import Screen
from turtle import Turtle
from paddle import Paddle
from ball import Ball
import time
from scorecard import Scorecard


screen = Screen()
paddle = Turtle()
ball = Ball()
scorecard = Scorecard()
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

# pong game screen setup
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.move_center()
        scorecard.l_point()
    
    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.move_center()
        scorecard.r_point()
        
        
        

screen.exitonclick()