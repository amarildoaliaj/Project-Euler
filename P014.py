def g(n):
    if (n % 4) == 1:
        return g((n - 1) / 4)
    else:
        return n


def prossimo(n):
    if (n % 4) == 0:
        return n / 4
    elif (n % 4) == 1:
        return 3 * g(n) + 1
    elif (n % 4) == 2:
        return n / 2
    else:
        return (3 * n + 1) / 2


partenza = 0
massimo = 0
for n in range(1, 1_000_000):
    p = n
    i = 0
    while n != 1:
        n = prossimo(n)
        i += 1
    if i > massimo:
        massimo = i
        partenza = p
print(partenza)
