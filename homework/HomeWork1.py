print('Hello user!')

try:
    a = input('Please type a number and click Enter\n')
    b = input('Please type another number and click Enter\n')
    c = a + b

    if a > b:
        print('First number is bigger than second one')
    elif a < b:
        print('Second number is bigger then first one')
    else:
        print('Numbers are equal')

    print ('The sum of numbers is: ' + str(c))

except:
    print('Only numbers are accepted')










