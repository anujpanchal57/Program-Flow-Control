# Example os WHILE loop
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

# WHILE loops can be best used for this
# available_exits = ["east", "south", "north east"]
#
# chosen_exit = ""
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please enter a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over !!")
#         break
#
# else:
#     print("Yaayy, you're out of there !!")

# Small Guessing Game

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Guess higher")
    else:
        print("Guess lower")
    guess = int(input())
    if guess == answer:
        print("You've guessed it correctly!!")
    else:
        print("Sorry, you've done it wrong")
else:
    print("You got it in the first shot !!!")