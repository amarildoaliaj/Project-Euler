def palindromo(n):
    a = n[::-1]
    if a == n:
        return True
    return False


somma = 0
for i in range(10**6):
    bino = "{0:b}".format(i)
    if palindromo(i.__str__()) and palindromo(bino.__str__()):
        somma += i
print(somma)
