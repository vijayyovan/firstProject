import os

# def dictonary(Key=Name, Value=value):
#     dic = {}
#     # dic[Key:Value]
#     # dic.append(Value)

dic = {}
bidding_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${highest_bid}")

def clear_screen():
    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

while not bidding_finished:
    Name = str(input("Enter the name"))
    value = int(input("what's the bid amount"))
    dic[Name] = value
    should_continue = input("please enter yes or no")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(dic)
    elif should_continue == "yes":
        clear_screen()











