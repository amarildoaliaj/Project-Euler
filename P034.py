import math

def Check(n):
    somma = 0
    for i in n:
        somma += math.factorial(int(i))
    if somma == int(n):
        return True
    return False

somma = 0
for i in range(3, 1000000):
    if Check(i.__str__()):
        somma += i
        print(i)
print(somma)

