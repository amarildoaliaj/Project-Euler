def IsPalindrome(n):
    a = str(n)
    b = a[len(a)::-1]
    if a == b:
        return True
    else:
        return False

max = 0
for i in range(1000):
    for j in range(1000):
        if (i*j) > max and IsPalindrome(i*j):
            max = i*j
print(max)