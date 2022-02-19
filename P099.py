from math import log10

valori = []
with open("file.txt", "r") as f:
    for i in range(1000):
        valori.append(f.readline().rstrip().split(','))
        valori[i][0] = int(valori[i][0])
        valori[i][1] = int(valori[i][1])

calcolati = []
for i in range(1000):
    base = valori[i][0]
    esponente = valori[i][1]
    calcolati.append(esponente * log10(base))
indice = calcolati.index(max(calcolati)) + 1
print(indice)
