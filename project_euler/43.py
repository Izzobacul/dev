import time

t = time.time()

def perm(lst):
    length = len(lst)
    if length == 0:
        yield []
    elif length == 1:
        yield lst
    else:
        for i in range(length):
            x = lst[i]
            xs = lst[:i] + lst[i + 1:]
            for p in perm(xs):
                yield [x] + p


def substring_divisibility(x):
    x = list(x)
    t = (int(f"{x[1]}{x[2]}{x[3]}") % 2 == 0 and
         int(f"{x[2]}{x[3]}{x[4]}") % 3 == 0 and
         int(f"{x[3]}{x[4]}{x[5]}") % 5 == 0 and
         int(f"{x[4]}{x[5]}{x[6]}") % 7 == 0 and
         int(f"{x[5]}{x[6]}{x[7]}") % 11 == 0 and
         int(f"{x[6]}{x[7]}{x[8]}") % 13 == 0 and
         int(f"{x[7]}{x[8]}{x[9]}") % 17 == 0)

    return t


# print(substring_divisibility('1406357289'))
data = [x for x in range(10)]
su = 0
# data = [1, 2, 3]

print('perms:')
for p in perm(data):
    print(p)
    s = "".join(map(str, p))
    x = int(s)
    if substring_divisibility(s):
        su += x
    print(su)

print(su)
print(time.time() - t)
