# for-loop session

# create a list of elements to iterate through
fruits = ['apples', 'banana', 'grape', 'pear', 'pineapples']
# for-loop to iterate through the list
for fruit in fruits:
    # print the elements in the list
    print(fruit)

# iterating through the list with an index
for fruit in range(len(fruits)):
    # prints the index and element of the list
    print('Fruit at ', fruit, 'is', fruits[fruit])

# for-loop to iterate through numbers
for i in range(1, 20 + 1):
    # print the numbers with the given range
    print(i)
    if i == 15:
        print('broke out of the for loop')
        break

# for-loop to iterate through numbers given in step
for i in range(0, 20 + 1, 2):
    # print the numbers with the given step and range
    print(i)
