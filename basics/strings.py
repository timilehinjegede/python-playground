# strings session

# a variable that holds a string
my_name = 'Timilehin'
# printing the value of variable my_name
print(my_name)
# printing a character at the specified index
print(my_name[4])
# printing the length of the string my_name
print(len(my_name))
# get substring of my_name
print(my_name[4:])
# get substring of my_name
print(my_name[0:4])  # same as print(my_name[:4])

# conversion of number to a string
num = 35
print(str(num))

# Working with strings methods
name = 'programming'
# capitalize the first character of the string
print(name.capitalize())
# get the index of the specified character
print(name.index('g'))
# convert the specified string to uppercase
print(name.upper())
# convert the specified string to lowercase
print(name.lower())
# checks if the specified variable is a string
print(name.isdigit())
# check if the specified string ends with the specified character
print(name.endswith('g'))
# replaced the specified character/characters with the existing character/characters
print(name.replace('programm', 'cod'))
# trims the string
print('      programming    '.strip())  # also .rstrip() and .lstrip()
# split the specified string using the separator
print(my_name.split('i'))
