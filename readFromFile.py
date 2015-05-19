__author__ = 'shannon'

# Reading from file with read().

readText = open('exampleFile.txt', 'r').read()
print(readText)

# Reading from file with readlines().

readT = open('exampleFile.txt', 'r').readlines()
print(readT)
