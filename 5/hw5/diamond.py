n = int(input("请输入n"))
for i in range(n+1):
    print(" "*(n-i), "*"*(2*i+1), " "*(n-i))
for i in range(n-1, -1, -1):
    print(" "*(n-i), "*"*(2*i+1), " "*(n-i))
