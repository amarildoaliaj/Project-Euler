x = 0
max = 0
for a in range(2, 100):
    for b in range(2, 100):
        lettere = str(a**b)
        for i in range(0, len(lettere)):
            x += int(lettere[i])
        if x > max:
            max = x
        x = 0
print(max)
