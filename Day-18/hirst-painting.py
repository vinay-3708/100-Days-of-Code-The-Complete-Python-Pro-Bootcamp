import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract("c:/Users/vinaymatam/Learning/Learning_Python/Day-18/download.jpg", 35)
color_list = []
for color in colors:
    color_tuple = (color.rgb.r,color.rgb.g,color.rgb.b)
    color_list.append(color_tuple)
#print(color_list)

tim = Turtle()
my_screen = Screen()
my_screen.colormode(255)
next_y_position = 0
tim.penup()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()
for x in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0)
my_screen.exitonclick()