a = 2**1000
b = str(a)
x = 0
for i in range(len(b)):
    x += int(b[i])
print(x)