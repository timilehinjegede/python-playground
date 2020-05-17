# dictionary session

# creating a dictionary
phone_book = {'tom': 12345, 'sam': 67890, 'ram': 16273}
# deleting entries in a dictionary
del phone_book['tom']
# iterating through the values of a dictionary
for key in phone_book:
    print('Key:', key, 'Value:', phone_book[key])
# another way of iterating through the values of a dictionary
for key, value in phone_book.items():
    print('Key:', key, 'Value: ', value)
# deleting all entries in a dictionary
# adding new entries to a dictionary
phone_book['tam'] = 93930
# phone_book.clear()
phone_book.clear()


# exploring more methods in the dictionaries
# printing the keys of the dictionary
print(phone_book.keys())
# printing the values of the dictionary
print(phone_book.values())
# gets the value of the specified key in the dictionary
print(phone_book.get('ram'))
