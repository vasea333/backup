def division(a,b):
    z = 0
    if ((a>0 and b>0)or(a<0 and b<0)):
        a=abs(a)
        b=abs(b)
        while (a>=b):
            z += 1
            a -= b
        return z
    elif (a<0 or b<0):
        a=abs(a)
        b=abs(b)
        while (a>=b):
            z += 1
            a -= b
        return -z
    return 0 if (a==0) else "Cannot divide by zero "
print division(0,10)