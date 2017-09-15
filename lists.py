# Example of COUNT
ipAddr = input("Please enter an IP Address: ")
print(ipAddr.count("."))

football_list = ["kind", "superstar", "record goalscorer"]
football_list.append("great father") # Appends the new record in the list

for state in football_list:
    print("Cristiano Ronaldo is "+ state)

# concatenating the list
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

number = even + odd

# Sorts the numbers automatically
number.sort()
print(sorted(number)) # In-built function in Python to sort the list
number_in_order = sorted(number)
print(number_in_order)

# We'll get the result as not equal because the lists contain the same numbers but they are in a
# different order
if number == number_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")

# This will give us the result that the lists are in order because we're sorting the numbers and comparing them
if number_in_order == sorted(number):
    print("The lists are equal")
else:
    print("The lists are not equal")

list_1 = []
list_2 = list()

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

if list_1 == list_2:
    print("Lists are equal")

print(list("Lists are equal"))


another_even = sorted(even, reverse=True) # Now the below stmt will return FALSE because another list EVEN is being
# created in a reversed format

# Returns TRUE because another_even and even are one and the same
print(another_even is even)

# This will return TRUE because it says that the contents are equal and not the order
print(another_even is even)
another_even.sort(reverse=True) # Reverses the original sequence
print(even)


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)
