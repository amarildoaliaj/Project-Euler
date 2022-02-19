import math

x = math.factorial(100).__str__()
massimoi = 0
for i in x:
    massimoi += int(i)
print(massimoi)
