# Small test prog
name = input("Please enter your name: ")
age = int(input("How old are you, {}".format(name)))
print(age)

# Asks to check whether the age is greater than or equal to 18
if age >= 18:
    print("You're an Adult !!")
    print("You can hop in for the movie")
else:
    print("Sorry, you can get back in {} years".format(18 - age))

# elif test prog
print("\n")
print("Please enter a number between 1 and 10: ")
guess = int(input())

if guess < 5:
    print("Please try to guess higher")
    guess = int(input())
    if guess == 5:
        print("You've done it, Kuddos")
    else:
        print("Sorry, try again later")
elif guess > 5:
    print("Please try to guess lower")
    guess = int(input())
    if guess == 5:
        print("You've done it, Kuddos")
    else:
        print("Sorry, try again later")
else:
    print("Kuddos, You've got it in the first time itself")

# Removing the duplication of code
print("Please enter a number between 1 and 10: ")
guess = int(input())

if guess != 5:
    if guess < 5:
        print("Guess higher")
    else: # guess should be lower
        print("Guess lower")

    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, better luck next time")
else:
    print("Kuddos, you did it in the first go")