import random
# Generate list 'l' with 30 random int elem. in range 0-99
l = random.sample(range(0, 99,), 30)
print(l)
# compute the number of even ints in the list "l"
number = 0
for i in l:
    if i % 2 == 0:
        number += 1
print(number)
