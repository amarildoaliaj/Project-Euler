variabile = 0


def fibo(n):
    '''calculate the n-th fibonacci number'''
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
    return b


def is_prime(n):
    if n in (2, 3):
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


def primes(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n % 6+6, 2-(n % 6 > 1)
    sieve = [True] * (n//3)
    for i in range(1, int(n**0.5)//3+1):
        if sieve[i]:
            k = 3*i+1 | 1
            sieve[k*k//3::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
            sieve[k*(k-2*(i & 1)+4)//3::2*k] = [False] * \
                ((n//6-k*(k-2*(i & 1)+4)//6-1)//k+1)
    return [2, 3] + [3*i+1 | 1 for i in range(1, n//3-correction) if sieve[i]]


def divisors(n):
    '''Proper Divisors (numbers less than n which divide evenly into n)'''
    p = list(x for tup in ([i, n // i] for i in range(1,
             int(n ** 0.5) + 1) if n % i == 0) for x in tup)
    # p.remove(n)
    return p
