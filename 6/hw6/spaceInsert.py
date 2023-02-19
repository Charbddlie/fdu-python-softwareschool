w = str(input("请输入:"))
for i in range(len(w)-1, 0, -1):
    print(w[0:i], w[i:])
for i in range(1, len(w)):
    print(w[0:i], w[i:])
