# Prints out the RANGE i.e., range(0, 100)
print(range(100))

# Gives a RANGE of 10 to a new list
my_list = list(range(10))
print(my_list)

# This helps to print out the Even and Odd lists
even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)

# INDEX examples
my_string = "Anuj Panchal"

# This will return 5
print(my_string.index('P'))
# This will return P
print(my_string[5])

small_decimals = range(0, 10)

# Prints out the range(0, 10)
print(small_decimals)
# Prints out '3'
print(small_decimals.index(3))

odd = range(1, 10000, 2)

# Prints out range(1, 10000)
print(odd)

# Prints out the number at the index '950'
print(odd[950])

# Gets the range of even number under 10000
evens = range(0, 10000, 2)
x = int(input("Please enter a positive number less than 10000: "))

# If the entered number is present in evens range, then print the below stmt
if x in evens:
    print("{} is divisible by evens".format(x))

print(small_decimals)

# Prints out the range(0, 10, 2)
my_range = small_decimals[::2]

print(my_range)
print(my_range.index(4))

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

# Prints out numbers between 3 and 40 with an index of 3
for i in my_range:
    print(i)

print("=" * 40)

# Prints out numbers between 3 and 40 with an index of 3
for i in range(3, 40, 3):
    print(i)

# Returns TRUE
print(my_range == range(3, 40, 3))
