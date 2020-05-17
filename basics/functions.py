# function session


# creating a function to calculate total of a person's expense
def calculate_total(exp):
    # variable to hold the total
    total = 0
    # for loop to iterate through the provided list
    for item in exp:
        total = total + item
        # return the total
    return total


# declaring a list of elements
tom_exp_list = [2100, 3400, 3500]
jim_exp_list = [200, 500, 700]

# calling the function and passing a list as an argument
toms_total = calculate_total(tom_exp_list)
jims_total = calculate_total(jim_exp_list)

# printing the value returned by the function
print('Tom\'s total expenses: ', toms_total)
print('Jim\'s total expenses: ', jims_total)
