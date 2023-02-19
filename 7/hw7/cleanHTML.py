import re
html = input("请输入html")
res = re.findall(r">.+<",html)
for i in res:
    print(i[1:-1])