def g(n):
    if (n % 4) == 1:
        return g((n-1)/4)
    if (n % 4) != 1:
        return n

def next(n):
    if (n % 4) == 0:
        return n/4
    elif (n % 4) == 1:
        return 3*g(n)+1
    elif (n % 4) == 2:
        return n/2
    else:
        return (3*n+1)/2

partenza = 0
max = 0
for n in range(1, 1_000_000):
    p = n
    i = 0
    while n != 1:
        n = next(n)
        i += 1
    if i > max:
        max = i
        partenza = p
print(partenza)
