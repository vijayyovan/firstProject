import random
import json
import game_data
# import pygame

# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     }]

from game_data import data
def value():
    random_item = random.choice(data)
    # for key, value in item.items():
    #     # print(f"{key}: {value}")
    #     if 'name' in item:
    (random_item['name'])
    a = int(random_item['follower_count'])
    return a

a = value()
print(a)

def value_b():
    random_item = random.choice(data)
    # for key, value in item.items():
    #     # print(f"{key}: {value}")
    #     if 'name' in item:
    (random_item['name'])
    a = int(random_item['follower_count'])
    return a

b = value_b()
print(b)

score = 0

print("Guess a letter a or b ")
guess = str(input("Enter a string"))
game_continue = True


while game_continue:
    if guess == "a":
        score += 1
        if a > b:
            print("you guessed right")
            print(f"your score is{score}")
            continue
    else:
        print("wrong answer")
        game_continue = False
    if guess == "b":
        score += 1
        if b > a:
            print("you guessed right")
            print(f"your score is {score}")
            continue
    else:
        print("wrong answer")
        game_continue = False



