import math
import time
import random

def verizni(a, b, c):
    # Izračuna verižni ulomek (a + sqrt(b))/c,
    # pri čemer je b nekvadrat. Rezultat je podan
    # v obliki tupla, kjer imamo najprej seznam, ki
    # predstavlja periodični verižni ulomek, potem 
    # pa še dolžino periode verižnega ulomka.
    z = math.sqrt(b)
    if z == math.floor(z):
        return 'Število b je kvadrat, vstavi za b nekvadrat!'
    if c == 0:
        return 'Z nič ne smemo deliti, za c vzemi neko drugo celo število!'
    p = a * abs(c)
    q = c * abs(c)
    d = b * c * c
    n = math.sqrt(d)
    a = (p + n) // q
    set1 = {(p,q)}
    list2 = [int(a)]
    list1 = [(p,q)]
    while True:
        p = q * a - p
        q = (d - p * p) // q
        a = (p + n) // q
        if (p, q) in set1:
            perioda = len(set1) - list1.index((p, q))
            return list2, perioda
        set1.add((p, q))
        list2.append(int(a))
        list1.append((p,q))

def generiraj_veliko_število(n):
    # generira naključno število z n-timi števkami
    
    x = 0
    for i in range(n):
        x += random.randrange(10) * 10**i
    return x

x = generiraj_veliko_število(15)
print(verizni(0, x, 1))
print(time.process_time())

# Za naključno 5-mestno število izračuna v 0.03125s.
# Za naključno 10-mestno število izračuna v 0.21875s.
# Za naključno 12-mestno število izračuna v 37.0625s.
# To se pravi, da moj program izračuna verižni ulomek do 10-mestnega števila v doslednem času.