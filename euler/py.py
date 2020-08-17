from math import sqrt

def divisorssum(n):
    s = 0
    for i in range(1, int(sqrt(n))):
        if n%i == 0:
            if n/i == i:
                s += i
            else:
                s += n/i
                s+= i
    return(s-n)

amicables = []

for i in range(1, 10000):
    if not i in amicables:
        for l in range(i+1, 10000):
            di = divisorssum(i)
            dl = divisorssum(l)
            if di == l and dl == i:
                if not i in amicables:
                    amicables.append(i)
                if not l in amicables:
                    amicables.append(l)
        print(amicables)

s = 0
for x in amicables:
    s += x
print(s)

