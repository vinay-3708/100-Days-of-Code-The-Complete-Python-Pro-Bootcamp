from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")
screen.bgpic("./blank_states_img.gif")

player = Turtle()
player.hideturtle()
player.penup()

data_file = "./50_states.csv"
df = pd.read_csv(data_file)
states_series = list(map(lambda x: x.upper(), df["state"].to_list()))
#print(states_series)
xcor = df["x"].to_list()
ycor = df["y"].to_list()
guessed_states = []
count = 0
is_game_on = True
while is_game_on:
    input = screen.textinput(f"{count}/50 States", "What's the another state name ?")
    if input ==  "quit":
        is_game_on = False
        states_to_learn = []
        for state in states_series:
            if state.upper() not in guessed_states:
                states_to_learn.append(state)
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
    if input.upper() in states_series and (input.upper() not in guessed_states):
        guessed_states.append(input.upper())
        index = states_series.index(input.upper())
        player.goto(xcor[index], ycor[index])
        player.write(df["state"].to_list()[index])
        count += 1



screen.exitonclick()