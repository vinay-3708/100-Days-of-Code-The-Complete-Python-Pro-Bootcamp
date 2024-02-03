import random
num = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
li = ["Rock","Paper","Scissors"]
cc = random.randint(0,2)
if num < 3:
    print(f"You choose {li[num]}")
    print(f"Computer choose {li[cc]}")
if num == cc:
    print("It's draw.")
elif num == 0 and cc == 1:
    print("You lose, Computer won.")
elif num == 0 and cc == 2:
    print("You won, computer lose.")
elif num == 1 and cc == 0:
    print("You won, computer lose.")
elif num == 1 and cc == 2:
    print("You lose, Computer won.")
elif num == 2 and cc == 0:
    print("You lose, Computer won.")
elif num == 2 and cc == 1:
    print("You won, computer lose.")
else:
    print("Invalid input. You lose.")