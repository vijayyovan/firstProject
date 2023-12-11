import  random
import os
from art import logo

print(logo)
print("Welcome to the number Guessing game!")

def computer_guess():
    guess = random.randint(1,100)
    return guess

com_guess = computer_guess()
print("enter the value of computer",com_guess)


user_input = str(input("please enter the difficulty easy or hard"))
if type(user_input) == str:
    print("Valid number")
else:
    print("Not a number")



i = 0
while i < 10:
    print("you have ", (10-i) ,"attempts remaining to guess the number")
    i = i + 1
    if user_input == "easy":
        user_guess = int(input("please enter the number"))
        if user_guess == com_guess:
            print("correct guessed")
            print("Great try!!")
            break
        elif user_guess > com_guess:
            print("too high")
        else:
            print("too low")
    if user_input == "hard":
        user_guess = int(input("please enter the number"))
        if user_guess == com_guess:
            print("correct guessed")
            print("Great try!!")
            break
        elif user_guess > com_guess:
            print("too high")
        else:
            print("too low")






