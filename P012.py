import Algorithms

for i in range(10**1000):
    t = i * (i + 1) / 2
    if (Algorithms.divisors(t).__len__()) > 500:
        print(int(t))
        break
