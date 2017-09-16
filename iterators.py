string = "0123456789"

for char in string:
    print(char)

my_iterator = iter(string)

# Returns the object value of the iterator
print(my_iterator)
# Returns the next values in the Iterator
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# And, if we add an extra print function for the next iterator, it will give us an error
print(next(my_iterator))

for char in string:
    print(char)

# Output will be the same as the output of FOR loop
for char in iter(string):
    print(char)
