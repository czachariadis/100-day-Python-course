# import turtle
# timmy = turtle.Turtle()

# ΑΝΤΙ ΓΙΑ ΑΥΤΟ:
from turtle import Turtle, Screen
timmy = Turtle()
# --------------------------
print(timmy)
timmy.shape("turtle")
timmy.color("cyan")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()