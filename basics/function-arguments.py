# function arguments


# positional arguments
def add_numbers_positional(a, b, c):
    return a + b + c


# named arguments
def add_numbers_named(a, b, c):
    return a + b + c


# default arguments
def add_numbers_default(a=3, b=4, c=3):
    return a + b + c


# calling the default argument function
print(add_numbers_default())
# calling the named arguments function
print(add_numbers_named(b=4, c=2, a=0))
# calling the positional arguments function
print(add_numbers_positional(4, 5, 8))
