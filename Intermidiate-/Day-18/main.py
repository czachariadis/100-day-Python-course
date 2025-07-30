from turtle import Turtle,Screen
from random import *

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")

timmy_turtle.speed(0)
timmy_turtle.pensize(2)

def random_color():
    r = random()
    g = random()
    b = random()
    return(r,g,b)

turns = randint(1,200)
RADIUS = 100
angle = 0

for i in range(turns):
    timmy_turtle.color(random_color())
    timmy_turtle.circle(RADIUS)
    timmy_turtle.setheading(angle)
    angle += 360 / turns

screen = Screen()
screen.exitonclick()