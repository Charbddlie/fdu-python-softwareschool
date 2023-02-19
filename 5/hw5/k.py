for i in range(1, 100001):
    for j in range(0, len(str(i))):
        l = i // 10**j
        r = i % 10**j
        if (l+r)**2 == i:
            print(str(i)+"=("+str(l)+"+"+str(r)+")**2")
