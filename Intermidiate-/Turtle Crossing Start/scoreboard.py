from turtle import Turtle


ALLIGMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 1
        self.goto(-220,260)
        self.write(f"Level: {self.level}", False, ALLIGMENT, FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.goto(-220,260)
        self.write(f"Level: {self.level}", False, ALLIGMENT, FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", False, ALLIGMENT, FONT)