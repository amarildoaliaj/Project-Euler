import Algorithms

a = Algorithms.divisors(600851475143)
b = []
for i in a:
    if Algorithms.is_prime(i):
        b.append(i)
print(max(b))