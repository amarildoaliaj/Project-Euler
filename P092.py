def Prossimo(n):
    x = 0
    a = str(n)
    for i in a:
        x += (int(i)*int(i))
    return x


p = 0
for i in range(1, 10_000_000):
    a = i
    while True:
        a = Prossimo(a)
        if a == 1:
            break
        if a == 89:
            p += 1
            break
print(p)
