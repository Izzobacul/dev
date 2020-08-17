from math import sqrt
def find_primes(n):
    primes = []
    for i in range(2, n+1):
        primes.append(i)
    for i in range(2, int(sqrt(n))):
        for p in primes:
            for j in range(p*2, n+1, p):
                if j in primes:
                    primes.remove(j)

    print(primes)

def is_circular(n):
    

find_primes(1000000)
