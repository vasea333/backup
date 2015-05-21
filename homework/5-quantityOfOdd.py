

def listOddQuantity(list1):

    list2 = []
    for i in list1:
        repeatNum = list1.count(i)

        if repeatNum % 2 != 0:
            list2.append(i)

    list3 = list(set(list2))
    return (list3)

list1 = [1, 2, 3, 3, 4]
print listOddQuantity(list1)