
max_sum = 2999

def primes(n):
	xs = [i for i in range(2, n+1)]
	primes = []
	running = True
	c = 0
	while running:
		for i in range(len(xs)):
			if xs[i] != 0:
				c = xs[i]
				break
		if c**c > n:
			for i in xs:
				if i != 0:
					primes.append(i)
			return(primes)
		for i in range(2*c, len(xs), c):
			xs[i] = 0

print(primes(10))