import time

def collatz_korak(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (3*n + 1) // 2

def collatz(n):
    i = 0
    while n != 1:
        n = collatz_korak(n)
        i += 1
    return i

def collatz_loop(n):
    for x in range(1,n):
        collatz(x)
    return

collatz_loop(100000)

#print(time.process_time())
#potrebuje 14s

#Domneva: za a <= 10**6 je potrebno najmanj 200 korakov.

def najvecje_stevilo_korakov(n):
    i = 0
    for x in range(1,n):
        y = collatz(x)
        i = max(i,y)
    return i

# domnevajmo kako izgleda funkcija za to, in potem izračunamo integral od 0 do 10**20

    