head = int(input("共有多少头？"))
foot = int(input("共有多少脚？"))
res = [(chi, rab) for chi in range(0, head+1)
       for rab in range(0, head+1) if rab+chi == head and rab*4+chi*2 == foot]
for (chi, rab) in res:
    print("鸡:", chi)
    print("兔:", rab)
