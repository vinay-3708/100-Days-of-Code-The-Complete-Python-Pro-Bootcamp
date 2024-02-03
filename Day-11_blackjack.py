import random

def deal_card():
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_deck)

def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list):
        return 0
    elif sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        return sum(card_list)
    return sum(card_list)


user_cards = []
computer_cards = []

for _ in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

