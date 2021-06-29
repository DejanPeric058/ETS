import math
import matplotlib.pyplot as plt


def fundamentalna_resitev(n):
    m = math.sqrt(n)
    x = int(m)
    if x == m:
        return 'Ni rešitve'
    p, q, a = 0, 1, x
    e1, e2 = 1, 0
    f1, f2 = 0, 1
    while True:
        p = a * q - p
        q = (n - p * p) // q
        a = (x + p) // q
 
        e1, e2 = e2, e1 + e2 * a
        f1, f2 = f2, f1 + f2 * a
 
        l, k = f2 * x + e2, f2
        if l * l - n * k * k == 1:
            return l, k

def potenciranje(a, b, d, k):
    x, y = 1, 0
    for _ in range(k):
        x, y = a * x + d * b * y, a * y + b * x
    return x, y

def absolutna_vrednost(a, b):
    return math.sqrt(a * a + b * b)

x, y, z = [], [], [] 
for d in range(2, 1000):
    a = math.sqrt(d)
    if math.floor(a) == a:
        continue
    x.append(d)
    e, f = fundamentalna_resitev(d)
    s = math.floor(absolutna_vrednost(e, f))
    y.append(s)
    z.append(math.log(s))
    #print(str(d) + ', ' + str(s))

plt.plot(x, y)
plt.yscale('log')
plt.show()
    
plt.plot(x, z)
plt.show()


# Ko narišemo prvi graf, ki kaže absolutno vrednost rešitve v
# odvisnosti od d vidimo, da je nekje določena vrednost prevelika
# glede na ostale, da bi lahko ocenili s kakšno funkcijo absolutna vrednost narašča.
# Ko absolutni vrednosti dodamo logaritem, lahko že bolje ocenimo, kako narašča absolutna
# vrednost glede na d. Sklepamo, da absolutna vrednost narašča eksponentno glede na d.

