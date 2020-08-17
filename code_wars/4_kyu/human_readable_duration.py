def format_duration(seconds):
    if seconds==0:
        return "now"
    t = [0, 0, 0, 0, 0]
    f = ""
    while seconds>=31536000:
        t[0]+=1
        seconds-=31536000
    while seconds>=86400:
        t[1]+=1
        seconds-=86400
    while seconds>=3600:
        t[2]+=1
        seconds-=3600
    while seconds>=60:
        t[3]+=1
        seconds-=60
    while seconds>0:
        t[4]+=1
        seconds-=1

    has = False

    for i, n in enumerate(t):
        if i==4 and n:
            ss = ["second", "seconds"][n-1 and 1]
            if has:
                f+=f" and {n} {ss}"
            else:
                f+=f"{n} {ss}"
        elif i==0 and n:
            yy = ["year", "years"][n-1 and 1]
            f+=f"{n} {yy}"
            has = True
        elif i!=4 and i!=0 and n:
            u = [["day", "days"], ["hour", "hours"], ["minute", "minutes"]][i-1][n-1 and 1]
            if has:
                if t[i+1]:
                    f+=f", {n} {u}"
                else:
                    f+=f" and {n} {u}"
            else:
                f+=f"{n} {u}"
                has = True

    return f
