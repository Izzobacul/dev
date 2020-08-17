def permutate(k, a, perms):
    if k == 1:
        perms.append("".join(a))
    else:
        permutate(k-1, a, perms)

        for i in range(0, k-1):
            if k&1:
                a[i], a[k-1] = a[k-1], a[i]
            else:
                a[0], a[k-1] = a[k-1], a[0]
            permutate(k-1, a, perms)
            
def noduplicates(arr):
    ret = []
    for n in arr:
        if not n in ret:
            ret.append(n)
    return(ret)

def permutations(string):
    chars = list(string)
    perms = []
    permutate(len(chars), chars, perms)
    return(noduplicates(perms))

print(permutations("123wqewq"))