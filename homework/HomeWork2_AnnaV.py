import random

# 1. Define empty list 'l';
l = []

# 2. Using 'for' loop append 9 elements of str type from '1' to '9' to list 'l';
for i in range(1, 10):
    l.append(str(i))

# 3. Transform list 'l' to string without any separation;
l = ''.join(l)

# 4. Using 'for' loop go through all elements in string 'l' and print
#    the result of multiplication by 2 of each element;
for x in l:
    print int(x) * 2

# 5. Remove element with index 3;
l = l[: 3] +  l[ 4:]

# 6. Add your name to the end of the string;
l += 'Anna'

# 7. Print the result.
print '\nResult: %s \n' % l

print '--------------------- HW Lesson 1 Problem 1-------------------------------------\n'

# 1. Generate list 'l' with 30 random int elements in range from 0 to 99;
# import random
l = []
for i in range(30):
    l.append(random.randint(0, 90))

print 'List with 30 random int elements in range from 0 to 99: '
print l

# 2. Compute the number of even ints in the given list 'l';
count = 0
for x in l:
    if x%2 == 0:
        #print x
        count += 1

# print the result.
print '\nThere are {0:2d} even integers in the given list\n'.format(count)

print '--------------------- HW Lesson 1 Problem 2 -------------------------------------\n'

# 1. Generate list 'l' with 30 random int elements in range from 0 to 99;
# See Problem 1
print 'List with 30 random int elements in range from 0 to 99: '
print l
# 2. Compute the difference between the largest and smallest
# values in the list, without using min(), max().
l.sort()
print '\nThe difference between the largest and smallest values in the list: ', l[len(l)-1] - l[0]

print '\n--------------------- HW Lesson 1 Problem 3 -------------------------------------\n'

s = 'fwerfgwfqawefwQafgeQfwefaqfeq'

# Return the number of times that the string 'qa' appears
# anywhere in the given string include upper case letters. For
# example 'Qa' and 'QA' count
search = 'qa'

print 'String \'%s \' appears %d times in \'%s\'.' % (search, s.lower().count(search), s)
print

print '\n--------------------- HW Lesson 1  -------------------------------------\n'

# Generate list 'l' with 200 random elements from 0 to 99 each;
print 'List with 200 random elements from 0 to 99 each:\n'
l = []
for i in range(200):
    l.append(random.randint(0, 90))

print l

#  Take an input from user. Input should be a number from 0 to 99

def input_validator(s):
    try:
        data = input(s)
        number = int(data)

#  If user provides number less then 0 or bigger then 99 print an error;
        if number > 99 or number < 0:
            print ('Error: number should be less then 0 or bigger then 99!!!')
            print number
        else:
            return number
    except ValueError:
    #  If user provides non-number print an error;
        print ('Except section: Error  ')

data = input_validator('\nPlease, provide a number from 0 to 99 >>> ')

count = l.count(data)
print '\nFound {0:2d} instances\n'.format(count)

if count > 0:
    end = len(l)
    position = -1
# Find all instances of that number in a list and print the amount and
# indexes of those instances.
    for i in range(count):
        position = l.index(data, position + 1, end)
        print 'Instance %s: position: %s  amount: %s ' % (i, position, l[position])

else: # If nothing found - print it.
    print 'No instances equal to {0:2d} were found in the list :'.format(data)
    print l

print '\n--------------------- HW Lesson 1 Task #1 -------------------------------------\n'

# You have a string 'I love milk'
s = 'I love milk'
# write a function which returns 'milk love I'
l = s.split(' ')
l.reverse()
s = ''
# - write this function in one-line
for x in l:
    s = s + x + ' '

# Extra
# - write a function which returns 'klim evol I'
s = 'I love milk'
print s[ : :-1] # using slicing

# without using slicing
def string_reverse(s):
    s_recerse = ''
    s_len = len(s)
    for i in range(s_len-1, -1, -1):
        #print i
        s_recerse += s[i]
    return s_recerse

print string_reverse(s)

print '--------------------- HW Lesson 1 Task #2 --------------------------------'

# 1. Define a none-empty list
l = [1,2,3,4,1,2,2,4]

# 2. write a function which prints only that objects the quantity of which is odd
#the function should print 3 and 2

def odd_count(l):
    distinctL = []
    for n in l:
        count  = l.count(n)
        if distinctL.count(n) == 0:
            distinctL.append(n)
            if count%2 == 1:
                print n

odd_count(l)