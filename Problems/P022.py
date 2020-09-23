def RitornaValore(x):
    return(ord(x)-64)

f = open("percorso", "r")
s = f.readline()
a = s.split(",")
s = []
for i in a:
    s.append(i[1:-1])
s.sort()

tot = 0
indice = 1
for i in s:
    somma = 0
    for k in range(len(i)):
        somma += RitornaValore(i[k])
    tot += (somma * indice)
    indice += 1
print(tot)