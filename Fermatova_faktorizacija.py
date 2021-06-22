import math
import time

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

	
print(fermat([85667124734235919999.0]))

print(time.process_time())