from turtle import Turtle
from math import *

IN_STEP = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid = 1, stretch_len = 1)
        self.penup()
        self.x_step = + IN_STEP
        self.y_step = + IN_STEP
    
    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)
        if (self.reaches_wall()):
            self.y_bounce()
    
    def reaches_wall(self):
        if (self.ycor() > 280 or self.ycor() < -280):
            return(True)
        
    def y_bounce(self):
        self.y_step *= -1
    
    def x_bounce(self):
        self.x_step *= -1

    def kick_off(self):
        self.goto(x = 0, y = 0)
        self.x_bounce()
        if (self.x_step < 0) :        
            self.x_step = -IN_STEP
        else:
            self.x_step = +IN_STEP