__author__ = 'shannon'

# Lists are mutable (changeable) sequences of objects.

fruits = ['apple', 'strawberry', 'kiwi']
for eachFruit in fruits:
    print(eachFruit)

# Print the first element.
print('\nFirst fruit', fruits[0])

# Append a new Element.
fruits.append('banana')

# Display new Elements.
for eachFruit in fruits:
    print(eachFruit)

# List constructor
newList = list('characters')
print('\n')
for list in newList:
    print(list)
