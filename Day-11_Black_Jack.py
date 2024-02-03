import random
print("\nWelcome to BlackJack Game...!!! \n")
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
usr_sum = 0
decker_sum = 0

def calc_sum(li):
    Sum = sum(li)
    if Sum > 21 and 11 in li:
        Sum = Sum - 11 + 1
    return Sum
    
def pick_card(player):
    new = random.choice(card_deck)
    player.append(new)
    return player

def compare_sum():
    print(f"DECKER_CARDS = {decker_cards}")
    print(f"USER_SUM = {usr_sum}")
    print(f"DECKER_SUM = {decker_sum}")
    if decker_sum > usr_sum:
        print("Decker Wins....")
    elif decker_sum < usr_sum:
        print("User Wins")
    else:
        print("It's a draw.....")

play_continue = True
usr_cards = random.choices(card_deck, k=2)
decker_cards = random.choices(card_deck, k=2)
print(f"USER_CARDS = {usr_cards}")
print(f"DECKER_CARDS = [{decker_cards[0]}, '_']")
usr_sum = calc_sum(usr_cards)
decker_sum = calc_sum(decker_cards)

if calc_sum(usr_cards) == 21:
    play_continue == False
    print("USER got Black Jack.........")
    
    compare_sum()
while play_continue == True:
    usr_input = input("'Hit' or 'stand': ")
    if usr_input == 'Hit':
        usr_cards = pick_card(usr_cards)
        print(f"USER_CARDS = {usr_cards}")
        usr_sum = calc_sum(usr_cards)
        decker_sum = calc_sum(decker_cards)
        if usr_sum > 21:
            print(f"DECKER_CARDS = {decker_cards}")
            print("Bust...Decker Wins...!")
            play_continue = False
        elif usr_sum == 21:
            print("Black Jack....")
            play_continue = False
            compare_sum()
    elif usr_input == 'stand':
        play_continue = False
        usr_sum = calc_sum(usr_cards)
        decker_sum = calc_sum(decker_cards)
        if usr_sum > 21:
            print(decker_cards)
            print("Bust...Decker Wins...!")
            play_continue = False
        else:
            while decker_sum < 17 and decker_sum < usr_sum:
                decker_cards = pick_card(decker_cards)
                print(f"DECKER_CARDS = {decker_cards}")
                decker_sum = calc_sum(decker_cards)
            if decker_sum > 21:
                print("Bust...You Win...!")
            else:
                compare_sum()