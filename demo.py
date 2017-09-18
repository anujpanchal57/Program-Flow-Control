# In Python, we can assign a single value to multiple variables
a = b = c = d = 10
print(b)

# We can also assign multiple values to multiple variables
a, b = 12, 13
print(a, b)

# 'a' gets the value of 'b' and 'b' gets the value of 'a'
# a is 13 & b is 12
a, b = b, a
print("a is {}".format(a))
print("b is {}".format(b))
