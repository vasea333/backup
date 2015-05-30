bulls=0
cows=0
l2=[2,3,2,3,4]
l1=[1,2,3,4,4]
l3=l1
l4=l2
for i in range(4):
    if l2[i] in l1:
        cows +=1
    elif l3[i] == l4[i]:
        bulls +=1
        del l1[i]
        del l2[i]
print cows, bulls