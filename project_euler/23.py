from itertools import combinations

def divs(n):
    divisors = 0
    if n % 2 == 0:
        divisors += n / 2
    for i in range(1, n//2):
        if n % i == 0:
            divisors += i
    return int(divisors)

abundants = []

for i in range(28123):
    d = divs(i)
    if d > i:
        abundants.append(i)
print(abundants)

sums = [sum(x) for x in combinations(abundants, 2)]
s = 0
for i in range(28123):
    if not i in sums:
        s += i

print(s)
