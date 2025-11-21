from art import logo
print(logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
Auction = True
bid = {}
winner = ''
highest_bid = 0
while Auction:
    name = input("Enter you name: ")
    price = int(input("Enter you price: "))
    bid[name] = price
    #  To check for the new bids
    Auction = input("Do you want to bid? y/n: ")
    if Auction == "y":
        Auction = True
    else:
        Auction = False
        for value in bid:
            if (bid[value] > highest_bid):
                highest_bid = bid[value]
                winner = value
        print(f"The winner of this auction is ",winner,"with the bid of",highest_bid)
# TODO-3: Whether if new bids need to be added

# TODO-4: Compare bids in dictionary


# new = {'astle': 100, 'anto': 200}
#
# print(new['astle'] > 100)