for i in range(1, 21):
    print(i)

# It is printing the numbers one by one
number = "9,223,372,036,854,775,807"
for i in range(0, len(number)): # len() is the property to give length
    print(number[i]) # This prints the number at the index position of i

# This code prints only the numbers ignoring the commas
# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     if number[i] in '0123456789': # Condition written for ignoring the commas
#         print(number[i])

# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     if number[i] in '0123456789': # Condition written for ignoring the commas
#         print(number[i], end='') # This will abort python from adding new line

# number = "9,223,372,036,854,775,807"
# cleanNumber = ''
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanNumber = cleanNumber + number[i] # Cleans off the commas and adds each number in the 'cleanNumber'
#
# newNumber = int(cleanNumber) # Converts cleanNumber into INT data type
# print("The number is {}".format(newNumber))

number = "9,223,372,036,854,775,807"
cleanNumber = ''

for char in number:
    if char in '0123456789':
        cleanNumber = cleanNumber + char

newNumber = int(cleanNumber)
print("The number is {}".format(newNumber))

# Example of how FOR Loop runs
for state in ["Green","Red","Blue"]:
    print("This parrot is " + state + ".") # We can also write the above statement as
    # print("This parrot is {}".format(state))

# Third field in this range argument tells us about the step (by much value we should skip the number)
for i in range(0, 100, 5):
    print("i is now {}".format(i))

# Multiplication in python
for i in range(1, 6):
    for j in range(1, 13):
        # By adding end='\t' it prints the result in a single line with tabs in bewtween
        print("{1} times {0} is {2}".format(i, j, i*j), end='\t')
    # print("------------------------")
    print('') # Adding a this blank line and commenting the above line will make the result print in a single line and
    # in a properly formatted manner
