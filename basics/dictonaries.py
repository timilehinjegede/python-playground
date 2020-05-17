# dictionary session

# creating a dictionary
phone_book = {'tom': 12345, 'sam': 67890, 'ram': 16273}
print(phone_book)
# adding new entries to a dictionary
phone_book['tam'] = 93930
print(phone_book)
# deleting entries in a dictionary
del phone_book['tom']
print(phone_book)
# iterating through the values of a dictionary
for key in phone_book:
    print('Key:', key, 'Value:', phone_book[key])
# another way of iterating through the values of a dictionary
for key, value in phone_book.items():
    print('Key:', key, 'Value: ', value)
# deleting all entries in a dictionary
phone_book.clear()
