def check(x):
    s = str(x)
    somma = 0
    for i in s:
        somma += int(i) ** 5
    if x == somma:
        return True
    return False


tot = 0
for i in range(2, 1000000):
    if check(i):
        tot += i
print(tot)
