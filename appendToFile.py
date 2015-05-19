__author__ = 'shannon'

# Append to a File.

appendText = '\nNew bit of intel'
appendFile = open('exampleFile.txt', 'a')

appendFile.write(appendText)
appendFile.close()