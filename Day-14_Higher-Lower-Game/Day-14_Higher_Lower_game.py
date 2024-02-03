import day14_higher_lower_game_data as g_data
import random
import os

data_len = len(g_data.data)
game_data = g_data.data
#print(game_data[0])
score = 0

def q_formation(name, des, country):
    vowels = ['a','e','i','o','u']
    if des[0].lower() in vowels:
        return f"{name}, an {des}, from {country}."
    else:
        return f"{name}, a {des}, from {country}."
    
def play_game():
    score = 0
    continue_game = True
    q1 = random.randint(0, data_len-1)
    while continue_game:
        print(g_data.logo)
        q2 = random.randint(0, data_len-1)
        is_q1_q2_same = True
        while is_q1_q2_same:
            if q1 == q2:
                q2 = random.randint(0, data_len-1)
            else:
                is_q1_q2_same = False
        q1_data = game_data[q1]
        q2_data = game_data[q2]
        question1 = q_formation(q1_data["name"], q1_data["description"], q1_data["country"])
        question2 = q_formation(q2_data["name"], q2_data["description"], q2_data["country"])
        print(f"\n Compare A: {question1}\n")
        print(g_data.vs)
        print(f"\n Compare B: {question2}\n")
        if q1_data["follower_count"] > q2_data["follower_count"]:
            answer = "A"
        elif q1_data["follower_count"] < q2_data["follower_count"]:
            answer = "B"
        else:
            print("It's a draw")
        usr_input = input("Who has more followers? Type 'A' or 'B': ").upper()
        if usr_input == answer:
            score += 1
            os.system('cls')
            q1 = q2
        else:
            continue_game = False
            print(f"You Lose, Your Score is {score}.")


play_game()