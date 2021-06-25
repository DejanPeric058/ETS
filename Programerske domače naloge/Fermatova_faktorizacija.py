import math
import time
import random

def faktoriziraj(n):
    # Število n faktorizira na princip iščemo tak t, da bo
    # t**2 - n popolni kvadrat y**2 => n = t**2 - y**2 = 
    # (t-y)*(t+y). 

	x = math.ceil(math.sqrt(n))
	y = x**2 - n
	while not math.sqrt(y).is_integer():
		x += 1
		y = x**2 - n
	return [x + math.sqrt(y), x - math.sqrt(y)]

def fermat(list):
    # Izračuna faktorizacijo na prafaktorje n, ki ga podamo
    # v enoelementnem seznamu.
    vmesni_faktorji = []
    prafaktorji = []
    for a in list:
        x, y = faktoriziraj(a)
        if y == 1:
            prafaktorji.append(x)
        else:        
            list.append(x)
            list.append(y)
    return prafaktorji


def generiraj_veliko_število(n):
    # generira naključno število z n števkami
    
    x = 0
    for i in range(n):
        x += random.randrange(10) * 10**i
    return x


x = generiraj_veliko_število(3)
print(fermat([x]))

print(time.process_time())