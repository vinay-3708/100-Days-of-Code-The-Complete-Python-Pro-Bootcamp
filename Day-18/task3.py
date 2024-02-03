from turtle import Turtle, Screen
import random
colors = ["red", "green", "black", "blue", "grey"]
tim = Turtle()
tim.shape("circle")
tim.pensize(10)
tim.speed(0)

def rand_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
directions = [0, 90, 180, 270]
my_screen = Screen()
my_screen.colormode(255)
for _ in range(100):
    tim.color(rand_color())
    tim.forward(50)
    tim.setheading(random.choice(directions))


#my_screen = Screen()
#my_screen.colormode(255)
my_screen.exitonclick()