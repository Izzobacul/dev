
def divs(n):
    divisors = 0
    if n % 2 == 0:
        divisors += n / 2
    for i in range(1, n//2):
        if n % i == 0:
            divisors += i
    return int(divisors)



xs = []

for i in range(10000):
    x = divs(i)
    xs.append(x)


ams = 0
for i, x in enumerate(xs):
    if x < 10000:
        if i == xs[x] and i != x:
            print(x)
            ams += x
print(ams)
