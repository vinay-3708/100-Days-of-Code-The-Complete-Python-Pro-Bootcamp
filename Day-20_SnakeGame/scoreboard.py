from turtle import Turtle, Screen

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__
        self.score = 0
        self.color("white")
        self.write(f"Score = {self.score}", move=False, align="center", font=('Arial', 8, 'normal'))