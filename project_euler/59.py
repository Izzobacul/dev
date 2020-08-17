import time
from itertools import combinations, permutations
import numpy as np

def xor(n, m):
    binn = f"{n:b}"
    binm = f"{m:b}"
    binn = f"{n:0{max(len(binn), len(binm))}b}"
    binm = f"{m:0{max(len(binn), len(binm))}b}"
    res = ""
    for i, b in enumerate(binn):
        bn = int(b)
        bm = int(binm[i])
        if (bn or bm) and (bn != bm):
            res += '1'
        else:
            res += '0'
    return(int(res, 2))

def no_duplicates(arr):
    for e in arr:
        if arr.count(e) > 1:
            arr.remove(e)
    return(arr)

def main():
    chars = open('p059_cipher.txt').read().split(',')
    a = [x for x in range(97, 123) for i in range(3)]
    combs = [x for x in combinations(a, 3)]
    combs = set(combs)
    keys = [[perm for perm in permutations(x)] for x in combs]
    keyss = []
    for i in keys:
        for l in i:
            keyss.append(l)
    keyss.append((123, 122, 122))
    kk = 0
    key = keyss[kk]
    k = 0
    print(len(keyss))
    strings = []
    while key != (123, 122, 122):
        string = ""
        for i in chars:
            x = xor(key[k], int(i))
            string += chr(x)
            k += 1
            if k==3:
                k = 0
        print(kk)
        strings.append(string)
        kk += 1
        key = keyss[kk]
    with open('59_decipher.txt', 'w') as out:
        out.write("\n".join(strings))

original = '''An extract taken from the introduction of one of Euler's most celebrated papers, "De summis serierum reciprocarum" [On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the entire sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if the true sum of this series is obtained, from it at once the quadrature of the circle follows. Namely, I have found that the sum of this series is a sixth part of the square of the perimeter of the circle whose diameter is 1; or by putting the sum of this series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the diameter. I will soon show that the sum of this series to be approximately 1.644934066842264364; and from multiplying this number by six, and then taking the square root, the number 3.141592653589793238 is indeed produced, which expresses the perimeter of a circle whose diameter is 1. Following again the same steps by which I had arrived at this sum, I have discovered that the sum of the series 1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely, the sum of this multiplied by 90 gives the biquadrate (fourth power) of the circumference of the perimeter of a circle whose diameter is 1. And by similar reasoning I have likewise been able to determine the sums of the subsequent series in which the exponents are even numbers.'''

if __name__ == '__main__':
    #main()
    print(original)
    su = 0
    for c in original:
        su += ord(c)
    print(su)
