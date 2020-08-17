p = ""
n = 1

while len(p) < 10:
	for i in range(1, n+1):
		p += str(9 * i)
	n += 1
	print(p)

print(p)