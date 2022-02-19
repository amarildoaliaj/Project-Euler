import Algorithms


def left(x, primi):
    while len(str(x)) > 1:
        x = int(str(x)[1:])
        if x not in primi:
            return False
    return True


def right(x, primi):
    while len(str(x)) > 1:
        x = int(str(x)[:-1])
        if x not in primi:
            return False
    return True


primi = Algorithms.primes2(800000)
valori = []
for i in primi:
    if left(i, primi) and right(i, primi):
        valori.append(i)
print(sum(valori[4:]))
