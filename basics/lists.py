# list session

# creating a list of fruits
fruits = ['banana', 'peach', 'orange', 'apple', 'grape']
# accessing a specific item in the list
print(fruits[3])
# mutating a list
fruits[0] = 'strawberry'  # changes the element at specified index to the assigned element
# adding values to the end of a list
fruits.append('pineapples')
# adding values to a specified position in the list
fruits.insert(2, 'pear')
# getting the index of a specified element in the list
print(fruits.index('pineapples'))
# accessing the last element of a list
print(fruits[-1])
# getting values of a list using the range method
print(fruits[2:6])
# joining two lists
drinks = ['pepsi', 'fanta', 'coke']
print(fruits+drinks)
# finding the length of the list
print(len(fruits))
# checking if an item is present in the list
print('pear' in fruits)  # returns a boolean
