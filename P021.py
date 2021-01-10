import Algorithms

def CheckAmicable(a):
    b = sum(Algorithms.Divisori(a))
    if sum(Algorithms.Divisori(b)) == a and a != b:
        return True
    return False

sum = 0
for a in range(1,10000):
    if CheckAmicable(a):
        sum += a
print(sum)

