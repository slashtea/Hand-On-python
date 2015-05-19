__author__ = 'shannon'

''' Dictionnaries are mutable mappings of keys to values.
    In other languages they are called associative arrays.
'''

# Creating a dictionary.
phoneUsers = {'Ziyad': '06 74 97 91 77', 'James': '256-5262-124'}

# Print the dictionary.
print(phoneUsers['Ziyad'])

# update dictionary.
phoneUsers['James'] = '256-5889-566'

# Print new dictionary.
print(phoneUsers)

# Another example.
capitales = {'England': 'London', 'Morocco': 'Rabat', 'Japan': 'Tokyo', 'Germany': 'Berlin'}

for capital in capitales:
    print(capitales[capital])