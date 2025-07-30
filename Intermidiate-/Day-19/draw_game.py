from turtle import Turtle,Screen


tim_turtle = Turtle()
screen = Screen()

def move_forwards():
    tim_turtle.forward(10)

def move_backwards():
    tim_turtle.backward(10)

def turn_count_clockwise():
    tim_turtle.left(1)

def turn_clockwise():
    tim_turtle.right(1)

def clear():
    tim_turtle.reset()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards,"s")
screen.onkey(turn_count_clockwise,"a")
screen.onkey(turn_clockwise,"d")
screen.onkey(clear,"c")

screen.exitonclick()