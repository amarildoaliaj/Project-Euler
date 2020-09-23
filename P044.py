# to fix

for i in range(1, 10000):
    pentagonals.add(int(i * (3 * i - 1) / 2))

for p1 in pentagonals:
    for p2 in pentagonals:
        if p1 + p2 in pentagonals:
            if p1 - p2 in pentagonals:
                print(p1 - p2)