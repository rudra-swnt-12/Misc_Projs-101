from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.go_up()
        self.go_down()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        self.speed("fastest")

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        self.speed("fastest")