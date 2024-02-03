from turtle import Screen, Turtle
import time
from snake import Snake

game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("Snake Game")
x_pos = 0
y_pos = 0
game_screen.tracer(0)

snake_1 = Snake()
game_screen.listen()
game_screen.onkey(key="Up", fun=snake_1.up)
game_screen.onkey(key="Down", fun=snake_1.down)
game_screen.onkey(key="Right", fun=snake_1.right)
game_screen.onkey(key="Left", fun=snake_1.left)


is_game_on = True
while is_game_on:
    time.sleep(0.2)
    game_screen.update()    
    snake_1.move()
game_screen.exitonclick()