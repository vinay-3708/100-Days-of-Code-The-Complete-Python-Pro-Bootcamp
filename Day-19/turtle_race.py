from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=400)
turle_colours = ["red", "orange", "yellow", "green", "blue", "purple"]
all_trutles = []

def create_turtles():
    for _ in range(len(turle_colours)):
        tim = Turtle()
        tim.shape("turtle")
        tim.color(turle_colours[_])
        tim.penup()
        new_y = -100 + ( _ * 40)
        tim.goto(x=-230, y=new_y)
        all_trutles.append(tim)

create_turtles()
usr_input = my_screen.textinput(title="Would you bet..", prompt="Which turtle will win? :")
is_race_on = True
while is_race_on:
    for turtle in all_trutles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() >= 220:
            turtle_postion = all_trutles.index(turtle)
            winner_turtle = turle_colours[turtle_postion]
            is_race_on = False
if usr_input == winner_turtle:
    print(f"Thats great guess, Your turtle '{winner_turtle}' wins the race")
else:
    print(f"Nah, Wrong guess, Turtle '{winner_turtle}' wins the race")
my_screen.exitonclick()