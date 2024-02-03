import os

print("\nWelcome to Secret Auction Program...!! \n")

bids_dict = {}
bid_completed = False

def bid_winner(bid_dist):
    highest_bid = 0
    for bidder in bid_dist:
        if bid_dist[bidder] > highest_bid:
            highest_bid = bid_dist[bidder]
            winner = bidder
    print(f"The winner is {winner} with bid of ${highest_bid}")

while not bid_completed:
    name = input("What's your name? : ")
    bid = int(input("What's your bid? : $"))
    bids_dict[name] = bid
    usr_input = input("Are there any other bidders who wants to bid? :").lower()
    if usr_input == "no":
        bid_completed = True
    os.system("cls")

bid_winner(bids_dict)