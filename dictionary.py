# A python dictionary.
exDic = {'Ahmed': [15, 'grey'], 'Yassine': [22, 'white'], 'Youness': [32, 'black']}
print(exDic)

# Print an exact value of a key.
print(exDic['Yassine'])

# Add an element.
exDic['Daoud'] = 14
print(exDic)

# delete an element.
del exDic['Daoud']
print(exDic)

# Get only hair color.
print(exDic['Youness'][1])