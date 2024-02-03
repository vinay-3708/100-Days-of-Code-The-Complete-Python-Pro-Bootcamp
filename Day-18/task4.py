from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed(0)
my_screen = Screen()
my_screen.colormode(255)

def rand_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

for _ in range(1,361):
    tim.color(rand_color())
    tim.circle(100)
    tim.right(_)
my_screen.exitonclick()