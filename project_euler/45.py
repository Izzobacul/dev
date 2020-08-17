import numpy as np

def triangle():
    n = 286

    while True:
        yield int(n * (n + 1) / 2)
        n += 1

def pentagonal():
    n = 166

    while True:
        yield int(n * (3*n - 1) / 2)
        n += 1

def hexagonal():
    n = 144

    while True:
        yield n * (2*n - 1)
        n += 1

t = triangle()
p = pentagonal()
h = hexagonal()

triangles = []
pentagons = []
hexagons = []

n = 0
found = False

for i in range(1000000):
    triangles.append(next(t))
    pentagons.append(next(p))
    hexagons.append(next(h))
    if triangles[n] in pentagons and triangles[n] in hexagons:
        print(triangles[n])
        found = True
        break
    n += 1

if not found:
    for i in triangles:
        if i in pentagons and i in hexagons:
            print(i)
            break
