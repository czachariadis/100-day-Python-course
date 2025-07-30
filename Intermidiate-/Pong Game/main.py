from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


game_is_on = True
screen = Screen()
screen.title("My Pong Game")
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

while (game_is_on):
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with a paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320):
        ball.x_bounce()
        ball.x_step -= 2
    if (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()
        ball.x_step += 2

    # Detect a scored goal for left
    if (ball.xcor() > 400):
        scoreboard.l_goal()
        ball.kick_off()

    # Detect a scored goal for right
    if (ball.xcor() < -400):
        scoreboard.r_goal()
        ball.kick_off()


screen.exitonclick()