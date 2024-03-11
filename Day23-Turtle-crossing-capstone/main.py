import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tortoise = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkeypress(key="Up", fun=tortoise.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(tortoise) < 20:
            game_is_on = False
            score.print_gameover()

    if tortoise.ycor() >= 280:
        score.print_updated_level()
        tortoise.goto(0, -280)
        cars.speed_up()


screen.exitonclick()
