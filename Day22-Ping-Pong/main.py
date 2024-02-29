from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

main_screen = Screen()
main_screen.setup(width=800, height=600)
main_screen.bgcolor("black")
main_screen.title("Pong")
main_screen.tracer(0)

paddle_1 = Paddle((350,0))
paddle_2 = Paddle((-350,0))
ball = Ball()

main_screen.listen()
main_screen.onkey(key="Up", fun=paddle_1.move_up)
main_screen.onkey(key="Down", fun=paddle_1.move_down)
main_screen.onkey(key="w", fun=paddle_2.move_up)
main_screen.onkey(key="s", fun=paddle_2.move_down)


game_on = True
while game_on:
    main_screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_1) < 60 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x() 

    if ball.xcor() > 350 or ball.xcor() < -350:
        #Score add and reset the ball
        ball.reset_position()
main_screen.exitonclick()