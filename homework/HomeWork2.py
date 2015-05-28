import random

l = random.sample(range(0, 100), 100)
l1 = random.sample(range(0, 100), 100)
l.extend(l1)
print l

userNum = None
while userNum == None:
    try:
        userInp = input('Please input a number in range 0-99\n')
        if not str(userInp).isdigit():
            print('Error: Only positive numbers are allowed')
        elif (userInp < 0 or userInp > 99):
            print("Error: Only numbers in range 0-99 are allowed")
        else:
            userNum = userInp

    except:
        print ('Error: Invalid input')

print "The amount of instances is: " + str(l.count(userInp))

for i in range(0, len(l)):
    if l[i] == userInp:
        print "The index of instance is: " + str(i)

print "User's input is: " + str(userInp)

