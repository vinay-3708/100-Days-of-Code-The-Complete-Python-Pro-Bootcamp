from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()



def mv_frwd():
    tim.forward(10)

def mv_bkwrd():
    tim.backward(10)

def clckwise():
    tim.right(10)

def anti_clckwise():
    tim.left(10)

def clr():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(mv_frwd, "w")
screen.onkey(key="s", fun=mv_bkwrd)
screen.onkey(key="a", fun=anti_clckwise)
screen.onkey(key="d", fun=clckwise)
screen.onkey(key="c", fun=clr)

screen.exitonclick()