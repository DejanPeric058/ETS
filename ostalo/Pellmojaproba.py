import math

def fundamental_solution(d):
    n = math.sqrt(d)
    a = math.floor(n)
    if n == a:
        return 1, 0
    x, y = 0, 1
    p, p0 = a, 1
    q, q0 = 1, 0
    while True:
        x = y * a - x
        y = (d - x * x) // y
        a = (x + n) // y
        p, p0 = a*p + p0, p
        q, q0 = a*q + q0, q
        if p * p - d * q * q == 1:
            return p, q

def potenciranje(a, b, d, k):
    x, y = 1, 0
    for _ in range(k):
        x, y = a * x + d * b * y, a * y + b * x
    return x, y

def absolutna_vrednost(a, b):
    return math.sqrt(a * a + b * b)

for d in range(2, 100):
    e, f = fundamental_solution(d)
    s = math.floor(absolutna_vrednost(e, f))
    print(str(d) + ', ' + str(s))


# popravi, za 61 ne izračuna!!!