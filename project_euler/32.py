from itertools import permutations

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0

for i in range(1, 9):
    for p in permutations(digits, i):
        l = [x for x in digits if not x in p]
        for j in range(1, 9-i):
            for pp in permutations(l, j):
                x = int("".join(map(str,pp))) * int("".join(map(str,p)))
                if all(not n in l and not n in pp for n in str(x)):
                    print(x)
                    sum += x
print(sum)
