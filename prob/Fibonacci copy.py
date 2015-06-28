def alex(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return alex(n-1)+alex(n-2)
print (alex(4))