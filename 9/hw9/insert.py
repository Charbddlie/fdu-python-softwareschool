def insert(lis:list,x):
    # return lis.sort()
    res = []
    x_i = 0
    for i in lis:
        if i>x:
            res.append(i)
        elif i ==x:
            res.insert(x_i,i)
        else:
            x_i+=1
            res.insert(0,i)
    return res
