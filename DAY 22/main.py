import time
from turtle import *

from ball import Ball
from paddle import Paddle
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ((ball.distance(right_paddle) < 50 and ball.xcor() > 320) or
            (ball.distance(left_paddle) < 50 and ball.xcor() < -320)):
        ball.bounce_x()

    # Detect ball out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        left_paddle.goto(-350, 0)
        right_paddle.goto(350, 0)
        scoreboard.left_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        left_paddle.goto(-350, 0)
        right_paddle.goto(350, 0)
        scoreboard.right_point()

screen.exitonclick()
