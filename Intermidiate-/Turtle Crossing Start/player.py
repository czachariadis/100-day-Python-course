from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def have_finished_level(self):
        if (self.ycor() > 280):
            return (True)
        
    def new_level(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)