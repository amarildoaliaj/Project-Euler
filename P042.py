def triangolare(n):
    return n*(n+1)/2


def calcola(parola):
    s = 0
    for i in range(len(parola)):
        s += (ord(parola[i])-64)
    return s


if __name__ == "__main__":
    tri = []
    for i in range(10**4):
        tri.append(triangolare(i))

    parole = []
    tot = 0
    with open("prova.txt") as file_in:
        for line in file_in:
            parole.append(line)
    parole = parole[0].split(',')
    for i in parole:
        valore = calcola(i.replace("\"", ""))
        if valore in tri:
            tot += 1
    print(tot)
