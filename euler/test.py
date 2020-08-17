def toBinary(n):
    bin = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(7, -1, -1):
        if n-2**i>=0:
            n-=2**i
            bin[i] = 1
    return(bin[::-1])

def fromBinary(s):
    n = 0
    s = s[::-1]
    for i, x in enumerate(list(s)):
        if int(x) == 1:
            n+= 2**i
    return(n)

print(fromBinary(toBinary(64)))