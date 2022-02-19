def calculatePerm(n):
    numeri = 0
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            for c in range(n):
                if c in (a, b):
                    continue
                for d in range(n):
                    if d in (a, b, c):
                        continue
                    for e in range(n):
                        if e in (a, b, c, d):
                            continue
                        for f in range(n):
                            if f in (a, b, c, d, e):
                                continue
                            for g in range(n):
                                if g in (a, b, c, d, e, f):
                                    continue
                                for h in range(n):
                                    if h in (a, b, c, d, e, f, g):
                                        continue
                                    for i in range(n):
                                        if i in (a, b, c, d, e, f, g, h):
                                            continue
                                        for j in range(n):
                                            if j in (a, b, c, d, e, f, g, h, i):
                                                continue
                                            else:
                                                numeri += 1
                                                if numeri == 10**6:
                                                    return str(
                                                        a.__str__()
                                                        + b.__str__()
                                                        + c.__str__()
                                                        + d.__str__()
                                                        + e.__str__()
                                                        + f.__str__()
                                                        + g.__str__()
                                                        + h.__str__()
                                                        + i.__str__()
                                                        + j.__str__()
                                                    )


n = 10
print(calculatePerm(n))
