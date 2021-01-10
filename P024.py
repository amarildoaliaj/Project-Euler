def CalculatePerm(n):
    numeri = 0
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            for c in range(n):
                if a == c or b == c:
                    continue
                for d in range(n):
                    if a == d or b == d or c == d:
                        continue
                    for e in range(n):
                        if a == e or b == e or c == e or d == e:
                            continue
                        for f in range(n):
                            if a == f or b == f or c == f or d == f or e == f:
                                continue
                            for g in range(n):
                                if a == g or b == g or c == g or d == g or e == g or f == g:
                                    continue
                                for h in range(n):
                                    if a == h or b == h or c == h or d == h or e == h or f == h or g == h:
                                        continue
                                    for i in range(n):
                                        if a == i or b == i or c == i or d == i or e == i or f == i or g == i or h == i:
                                            continue
                                        for j in range(n):
                                            if a == j or b == j or c == j or d == j or e == j or f == j or g == j or h == j or i == j:
                                                continue
                                            else:
                                                numeri += 1
                                                if numeri == 10 ** 6:
                                                    return str(a.__str__()+b.__str__() +c.__str__() +d.__str__() +e.__str__() +f.__str__() +g.__str__() +h.__str__() +i.__str__() +j.__str__())

n = 10
print(CalculatePerm(n))

