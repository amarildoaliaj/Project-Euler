def Palindromo(n):
    a = n[::-1]
    if a == n:
        return True
    return False

sum = 0
for i in range(10**6):
    bin = "{0:b}".format(i)
    if Palindromo(i.__str__()) and Palindromo(bin.__str__()):
        sum += i
print(sum)

