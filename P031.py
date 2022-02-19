A = 0


def calcola(a):
    return (
        a[0] * 1 + a[1] * 2 + a[2] * 5 + a[3] * 10 + a[4] * 20 + a[5] * 50 + a[6] * 100
    )


def back(a, s, n):
    c = calcola(a)
    if c > 200:
        return
    if s == n:
        if c == 200:
            global A
            A += 1
        return

    for i in range(201):
        b = a[s]
        a[s] = i
        back(a, s + 1, n)
        a[s] = b
    return


if __name__ == "__main__":
    a = [0, 0, 0, 0, 0, 0, 0]
    back(a, 0, 7)
    print(A)
