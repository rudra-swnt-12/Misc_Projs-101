import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up" )

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_create()
    car_manager.move_cars()

    #Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing
    if player.finish_line_reach():
        player.start_position()
        car_manager.level_up()
        scoreboard.level_increase()

screen.exitonclick()