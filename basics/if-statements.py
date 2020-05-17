# if else statements

# accept input from a use
number = input('Enter a number: ')

# convert the accepted string to an integer and test for a condition
if int(number) == 0:
    # print if the user input was a zero
    print('number entered is zero')
elif int(number) % 2 == 0:
    # print if the condition is met
    print(number, 'is even')
else:
    # print if the condition is not met
    print(number, 'is odd')
