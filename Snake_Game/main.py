from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Python Dash")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    #Detect collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()