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

# Examples of IF & AND keywords
age = int(input("How old are you ? "))

# Incase of AND stmt, python checks both the conditions and if they're true then only the loop will execute
if (age >= 18) and (age <= 60):
if 18 <= age <= 60:
    print("Have a good day working !!")

# Whereas incase of OR stmt, python checks only any one of the two conditions and if any one of them evaluates to true
# Then if will run the IF loop otherwise it will jump to the ELSE loop
if (age < 18) or (age > 60):
    print("Enjoy your life")
else:
    print("Have a good day working!!!")

# Example of FALSE stmts
x = input("Please enter something : ")

# If you enter anything this loop will be executed
if x:
    print("You entered '{}'".format(x))
else:
    print("You didn't enter anything!!")

# Example of NOT
print(not True)
print(not False)

age = int(input("How old are you ? "))

if not(age < 18):
    print("Hurray, You can vote !!")
    print("Please put X in the box")
else:
    print("Please come back in {} years !".format(18 - age))

# Example of IN keyword
parrot = "Cute Bird"

letter = input("Please enter a character : ")

if letter not in parrot:
    print("Sorry, i don't need that letter")
else:
    print("Give me {}, Anuj".format(letter))
