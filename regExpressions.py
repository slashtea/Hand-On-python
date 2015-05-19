import re

exampleString = '''
Jessica is 15 years old.
'''

'''
    Identifiers.

    \d: any number.
    \D: anything but a number.
    \s: space.
    \S: anything but a space.
    \w: any character.
    \W: anything but a character.
    . any character except for a new line.
    \b: the whitespace around words.
    \.: a period.

    Modifiers.

    ?: 0 or 1.
    []: range or variance.
'''

# To notify python this is going to be a regular expression, use 'r'.
ages = re.findall(r'\d{1,3}', exampleString)

# Printing out the matched expression from exampleString.
print(ages)