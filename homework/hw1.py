from random import randint


def main():
    print revwords('I love milk')
    print reversall('I love milk')
    print odd([1,2,3,4,1,2,2,4])
    print 'Number of even ints in the list is ' + str(evens())
    print 'Difference between the largest and smallest values is ' + str(maxn())
    print 'Number of times is', qatimes('fwerfgwfqawefwQafgeQfwefaqfeq','qa')
    homework()

# Task #1 revert only words in - I love milk
def revwords(text):
    text = text.split()
    s = ''
    for i in xrange(len(text) - 1, -1, -1):
        s = s+" "+text[i]
    return s[1:]

# Task #1 (extra) revert all in - I love milk
def reversall(text):
    if len(text) <= 1:
        return text
    return reversall(text[1:]) + text[0]

# Task 2
def odd(l):
    f=[]
    for i in l:
        if not l.count(i) % 2 == 0 and i not in f:
            f.append(i)
    f.reverse()
    return ' and '.join(str(x) for x in (f))

# problem 1
def evens():
    x = []
    l = [randint(0, 99) for p in range(0, 30)]
    evens.l = l
    [x.append(i) if i % 2 == 0 and i != 0 else i for i in l]
    return len(x)

# problem 2
def maxn():
    l = evens.l
    l = sorted(l)
    return l[29]-l[0]

# problem 3
def qatimes(x, y):
    a = list(x.lower())
    count = 0
    for i in range(0, len(a)-1):
        if a[i] + a[i+1] == y:
            count += 1
    return count

# problem homework
def homework():
    l = [randint(0, 99) for p in range(0, 200)]
    r = []
    user = raw_input('Please type number betwin 0 and 99 ')
    if user.isdigit() and 0 <= int(user) <= 99:
        useri = int(user)
        for s, j in enumerate(l):
            if j == useri:
                r.append(s)
        if len(r) == 0:
            print 'Number %d is not present in the list' % useri
        else:
            print "The amount of %d in list is %d and index or indexes is " % (useri, len(r),) + str(r).strip('[]')
    else:
        print 'error'


if __name__ == "__main__":
    main()