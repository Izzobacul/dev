xs = []
xss = ""
i = 0
while len(xss) < 100000:
    xs.append(i)
    xss += str(i)
    i += 1
print(xss)
print(int(xss[1]) *
      int(xss[10]) *
      int(xss[100]) *
      int(xss[1000]) *
      int(xss[10000]) *
      int(xss[100000]) *
      int(xss[1000000]))
