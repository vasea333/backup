'''
str1 = 'I love milk'

list1 = str1.split(' ')
list1.reverse()

print (list1)

str2 = ' '.join(list1)
print (str2)
'''

def reverseString(str1):
    return ' '.join((str1.split(' '))[::-1])
print (reverseString('I Love Milk'))
