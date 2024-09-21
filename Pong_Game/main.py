from turtle import Screen
from paddle import Paddle
from ball import  Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed) #0.040 is a good speed
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    #Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()

    #Detect if ball misses r_paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if ball misses l_paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()