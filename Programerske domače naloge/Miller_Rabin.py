import random
import time


def Miller_Rabin(n,k):
    # Za število n preveri za k naključno izbranih osnov med
    # 1 in n-1 Millerjev test praštevilskosti. Če dobimo True 
    # za k = 100, je število skoraj zagotovo praštevilo.
    if n == 1:
        return False
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    for _ in range(k):
        x = random.randrange(1,n-1)
        if not Miller_test(n, x, d, s):
            return False
    return True

def Miller_test(n, a, d, s):
    # Za n preverimo Millerjev test praštevilskosti z osnovo a.

    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for r in range(s-1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False

def generiraj_veliko_število(n):
    # generira naključno število z n-timi števkami
    
    x = 0
    for i in range(n):
        x += random.randrange(10) * 10**i
    return x
    

#for i in range(10000):
#    x = generiraj_veliko_število(200)
#    if Miller_Rabin(x,100):
#        print(str(x) + ' je zelo veliko praštevilo')
#        break
#
#print(time.process_time())

# 8566712473423591964391266237285135649296285643131777558249965988547586767374857358265707623711378495068205739828446554665555352300145752918959323904535138953003300721822058937358698753247079931948389 je zelo veliko praštevilo