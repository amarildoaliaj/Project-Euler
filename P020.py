import math

x = math.factorial(100).__str__()
max = 0
for i in x:
    max += int(i)
print(max)