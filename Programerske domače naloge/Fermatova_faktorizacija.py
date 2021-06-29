import math
import time
import random
from Miller_Rabin import Miller_Rabin

def faktoriziraj(n):
	# Število n faktorizira na princip iščemo tak t, da bo
	# t**2 - n popolni kvadrat y**2 => n = t**2 - y**2 = 
	# (t-y)*(t+y).
	
	if Miller_Rabin(n, 100):
		return n, 1
	x = math.ceil(math.sqrt(n)) 
	y = x**2 - n
	while True:
		z = math.sqrt(y)
		if z == int(z):
			return int(x + z), int(x - z)
		x += 1
		y = x**2 - n
		
	

def fermat(n):
    # Izračuna faktorizacijo na prafaktorje n.

		
	dvojke = []
	while n % 2 == 0:
		n //= 2
		dvojke.append(2)
	prafaktorji = [n]
	list1 = []
	for a in prafaktorji:
		x, y = faktoriziraj(a)
		if y != 1:
			prafaktorji.append(x)
			prafaktorji.append(y)
			list1.append(a)
	for j in list1:
		prafaktorji.remove(j)
	prafaktorji += dvojke
	return prafaktorji


def generiraj_veliko_število(n):
	# generira naključno število z n števkami
		
	x = 0
	for i in range(n):
		x += random.randrange(10) * 10**i
	return x


x = generiraj_veliko_število(10)
for i in range(10**9,10**9):
	faktorji = fermat(i)
	niz = str(i) + ' = ' + str(faktorji[0])
	for s in faktorji[1:]:
		niz += ' * ' + str(s)
	print(niz)
print(x)
faktorji = fermat(x)
niz = str(x) + ' = ' + str(faktorji[0])
for s in faktorji[1:]:
	niz += ' * ' + str(s)
print(niz)

print(time.process_time())