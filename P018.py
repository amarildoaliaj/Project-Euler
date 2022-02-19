def golden_pyramid_d(triangle):
    tr = [row[:] for row in triangle]  # copy
    for i in range(len(tr) - 2, -1, -1):
        for j in range(i + 1):
            tr[i][j] += max(tr[i + 1][j], tr[i + 1][j + 1])
    return tr[0][0]


matrice = []
with open("file.txt", "r") as f:
    for i in range(15):
        matrice.append(f.readline().rstrip().split(" "))

for i in range(15):
    for j in range(i, 15):
        matrice[j][i] = int(matrice[j][i])

print(golden_pyramid_d(matrice))
