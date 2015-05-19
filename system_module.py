# Playing around with sys module.

import sys

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

# Getting to argv, can also use that to communicate with other languages.
print('This is argv:', sys.argv)

# Some testing
if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print('Only one argument provided')