x = 0
massimo = 0
for a in range(2, 100):
    for b in range(2, 100):
        lettere = str(a**b)
        for i in range(0, len(lettere)):
            x += int(lettere[i])
        if x > massimo:
            massimo = x
        x = 0
print(massimo)
