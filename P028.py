def altoDestra(x):
    return 4 * x * x + 4 * x + 1


def bassoDestra(x):
    return 4 * x * x - 2 * x + 1


def bassoSinistra(x):
    return 4 * x * x + 1


def altoSinistra(x):
    return 4 * x * x + 2 * x + 1


somma = 1
for i in range(1, 501):
    somma += altoDestra(i)
    somma += bassoDestra(i)
    somma += altoSinistra(i)
    somma += bassoSinistra(i)
print(somma)
