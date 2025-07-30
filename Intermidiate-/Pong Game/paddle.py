from turtle import Turtle


STEP = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + STEP
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - STEP
        self.goto(self.xcor(), new_y)    