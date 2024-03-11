from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.LEVEL = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-220, 240)
        self.write(f"Level: {self.LEVEL}", align="center", font=FONT)


    def print_updated_level(self):
        self.clear()
        self.LEVEL += 1
        self.write(f"Level: {self.LEVEL}", align="center", font=FONT)
    
    def print_gameover(self):
        self.goto(0,0)
        self.write("GAME-OVER...!", align="center", font=FONT)