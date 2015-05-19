import os, time

curDir = os.getcwd()
print(curDir)

# Create a new dir.
os.mkdir('newDir')

time.sleep(2)

# Rename the directory.
os.rename('newDir', 'osdirectoryRenamed')

time.sleep(2)

# Delete the directory.
os.rmdir('osdirectoryRenamed')