number = "9, 14, 30, 29, 50"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        # Also called as Augmented Assignment, you can also use the normal method
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

# Examples of Augmented Assignment

# Addition
x = 15
x += 5
print(x)

# Subtraction
x -= 5
print(x)

# Multiplication
x *= 4
print(x)

# Division
x /= 6
print(x)

# Power
x **= 2
print(x)

# Mod or Remainder
x %= 9
print(x)

# Concatenation Examples
greeting = "Good"
greeting += " Morning "
print(greeting)

greeting *= 5
print(greeting, "\t")