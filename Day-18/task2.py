from turtle import Turtle, Screen

tim = Turtle()
for _ in range(3,9):
    for x in range(0,_):
        tim.forward(100)
        angle = 360/_
        tim.right(angle)

my_screen = Screen()
my_screen.exitonclick()