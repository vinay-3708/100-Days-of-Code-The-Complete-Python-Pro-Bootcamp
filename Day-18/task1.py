from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")

for _ in range(4):
    tim.forward(100)
    tim.left(90)

tim.penup()
tim.right(90)
tim.forward(20)

tim.left(90)

for _ in range(20):
    tim.pendown()
    tim.forward(5)
    tim.penup()
    tim.forward(5)

my_screen = Screen()
my_screen.exitonclick()