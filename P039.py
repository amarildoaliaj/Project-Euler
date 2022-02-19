def Rettangolo(a, b, c):
    """torna True se rettangolo"""
    if a**2 + b**2 == c**2:
        return True
    return False


dizionaio = {}
for p in range(1000, 1, -1):
    rettangoli = 0
    print("\nP = " + p.__str__())
    for a in range(1, p):
        for b in range(a, p):
            if a + b > p or (a * b / 2) % 6 != 0:
                continue
            for c in range(b, p):
                if a + b > c and a + b + c == p and Rettangolo(a, b, c):
                    rettangoli += 1
                    print(
                        "RETTANGOLO: "
                        + a.__str__()
                        + "/"
                        + b.__str__()
                        + "/"
                        + c.__str__()
                    )

    dizionaio[p] = rettangoli
print(sorted(dizionaio.items(), key=lambda x: x[1], reverse=True))
# Vengono stmpati in ordine decrescente, quindi la risposta e la prima
