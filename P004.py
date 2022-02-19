def IsPalindrome(n):
    a = str(n)
    b = a[len(a) :: -1]
    return bool(a == b)


massimo = 0
for i in range(1000):
    for j in range(1000):
        if (i * j) > massimo and IsPalindrome(i * j):
            massimo = i * j
print(massimo)
