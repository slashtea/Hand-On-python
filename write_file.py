__author__ = 'shannon'

#Writing into a file.

text = 'text to write\nIt is great!'
saveFile = open('exampleFile.txt', 'w')

saveFile.write(text)
saveFile.close()