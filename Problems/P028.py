def AltoDestra(x):
    return 4*x*x+4*x+1
def BassoDestra(x):
    return 4*x*x-2*x+1
def BassoSinistra(x):
    return 4*x*x+1
def AltoSinistra(x):
    return 4*x*x+2*x+1

somma = 1
for i in range(1,501):
    somma += AltoDestra(i)
    somma += BassoDestra(i)
    somma += AltoSinistra(i)
    somma += BassoSinistra(i)
print(somma)
