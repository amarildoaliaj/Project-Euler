def divisible(n):
    for i in range(11, 21):
        if n % i != 0:
            return False
    return True


i = 0
while True:
    if divisible(i):
        print(i)
        break
    i += 1
