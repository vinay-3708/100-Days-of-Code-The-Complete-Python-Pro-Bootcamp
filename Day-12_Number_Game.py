import random
logo = """
_______               ___.                    ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/     \/      \/     \/ 

"""

print(logo)

num = random.randint(1,100)
print("I'm thinking a number between 1 and 100.")

def lives():
    choice = input("Choose diffculty: Type 'easy' or 'hard': ")
    if choice == 'easy':
        return 10
    else:
        return 5
    

def validate(usr_input):
    if usr_input > num:
        print("Too high")
    elif usr_input < num:
        print("Too low")

def reduce_life(life):
    return life-1

def play_game():
    stop_game = False 
    num_of_lives = lives()
    print(f"You have {num_of_lives} attempts to guess the number.")
    while not stop_game:
        usr = int(input("Make a guess: "))
        validate(usr)
        if usr == num:
            print(f"Yes, you guess the correct number {num}.")
            stop_game = True
        else:
            num_of_lives = reduce_life(num_of_lives)
            if num_of_lives > 0:
                print(f"You have {num_of_lives} attempts to guess the number.")
            else:
                print("You lost all lives.")
                stop_game = True

play_game()