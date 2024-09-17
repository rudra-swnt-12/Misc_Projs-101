from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title= "Make your bet \n", prompt="Which turtle will win the race?. Enter your color among VIBGYOR: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_Turtle = Turtle(shape="turtle")
    new_Turtle.color(colors[turtle_index])
    new_Turtle.penup()
    new_Turtle.goto(x= -230, y= y_positions[turtle_index])
    all_turtles.append(new_Turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congrats!, {winning_color} has won the race!")
            else:
                print(f"Sorry! {winning_color} has won the race! You lost")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()