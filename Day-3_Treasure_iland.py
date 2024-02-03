print("Welcome to Treasure Island.Your mission is to find the treasure.")
first = input('You are at cross-road. Type "left" or "right" ? ')
if first == "left":
    second = input("You are at lake, Swim or Wait ? ")
    if second.lower() == "wait":
        third = input("Which door ? Red/Yellow/Blue? ")
        if third.lower() == "red":
            print("Burned by fire, Game over! ")
        elif third.lower() == "yellow":
            print("You Won!")
        elif third.lower() == "blue":
            print("Eaten by beast, Game over!")
        else:
            print("Game over!")
    else:
        print("Attacked by trout, Game over!")
else:
    print("You fell into a hole, Game over!")