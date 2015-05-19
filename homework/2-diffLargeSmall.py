__author__ = 'aleh'

import random

# generate list 'l' with 30 random int elem in range 0-99

l = random.sample(range(0, 99), 30)
print (l)

minElem = l[0]
maxElem = 0
for i in l:

    if i > maxElem:
        maxElem = i
        # print (maxElem)
    elif i <= minElem:
        minElem = i
        # print (minElem)
difLargeSmal = maxElem - minElem
print ('Largest - Smallest = ' + str(difLargeSmal))

