import math

def Triangolare(n):
    return n*(n+1)/2

def CheckPent(n):
    x = (math.sqrt(24*n+1)+1)/6
    if x.is_integer():
        return True
    else:
        return False

def CheckHex(n):
    x = (math.sqrt(8*n+1)+1)/4
    if x.is_integer():
        return True
    else:
        return False

for i in range(286,100000):
    t = Triangolare(i)
    if CheckPent(t):
        if CheckHex(t):
            print(t.__int__())
            break


