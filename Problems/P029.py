elementi = set()
for a in range(2,101):
    for b in range(2,101):
        elementi.add(a**b)
print(len(elementi))