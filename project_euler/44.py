def pentagonal(n):
	p = []
	for i in range(1, n + 1):
		p.append(int(i * (3 * i - 1) / 2))
	return p


pentagonals = pentagonal(10000)

mi = float('inf')

for x, i in enumerate(pentagonals):
	for j in pentagonals[x:]:
		if i + j in pentagonals and j - i in pentagonals:
			print('dab')
		if i + j in pentagonals and j - i in pentagonals and j - i < mi:
			print(i, j, j - i)
			mi = j - i

print(mi)
