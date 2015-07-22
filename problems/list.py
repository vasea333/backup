import random



l = range(1, 11)
for i in range(0, len(l)):
    print (l[i] * 2)
    l[i] = l[i]*2
l.reverse()

while 4 in l:
    l.remove(4)
l.pop(3)
l.sort()
l.append('Oleg')
print(l)
## the end

#random list
f = [random.randrange(1, 10) for _ in range(0, 4)]





