def is_pitagora(a,b,c):
    if (a*a + b*b) == (c*c):
        return True

x = []
for a in range(1,1000):
    for b in range(a,1000):
        for c in range(b,1000):
            if (a+b+c) == 1000:
                if is_pitagora(a,b,c):
                    print(a*b*c)