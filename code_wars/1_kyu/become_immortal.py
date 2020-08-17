def xor(a, b, l):
    le = max(len((f"{a:b}")), len(f"{b:b}"))
    a = f"{a:0{le}b}"
    b = f"{b:0{le}b}"
    x = ""
    for i, d in enumerate(a):
        if (d=='1' and b[i]=='0') or (b[i]=='1' and d=='0'):
            x += '1'
        else:
            x += '0'
    x = int(x, 2)
    x = x-l if x-l>=0 else 0
    return(x)

def elder_age(m,n,l,t):
    worshippers = [[xor(i, j, l) for i in range(0, m)] for j in range(0, n)]
    s = 0
    for l in worshippers:
        s += sum(l)
    if s>=t:
        return(s-(t*(s//t)))
    else:
        return(s)

#print(elder_age(8,5,1,100), 5)
#
#print(elder_age(8,8,0,100007), 224)
#print(elder_age(25,31,0,100007), 11925)
#print(elder_age(5,45,3,1000007), 4323)
#print(elder_age(31,39,7,2345), 1586)
#print(elder_age(545,435,342,1000007), 808451)
print(elder_age(28827050410, 35165045587, 7109602, 13719506), 5456283)