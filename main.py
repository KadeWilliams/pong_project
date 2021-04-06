from paddle import Paddle
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.tracer(0)
screen.title('Pong')

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

is_game_running = True
while is_game_running:
    screen.update()
    time.sleep(ball.move_speed)

    # Detect collision with top and bottom walls
    ball.move()

    # Detect collision with paddle
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 320 or ball.distance(l_paddle) <= 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() >= 390:
        scoreboard.left_increase()
        ball.reset_position()


    # Detect when left paddle misses
    if ball.xcor() <= -390:
        scoreboard.right_increase()
        ball.reset_position()



screen.exitonclick()
