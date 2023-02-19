a, b = str(input("请输入两个单词，以空格分隔")).split(" ")
print("单词", a, "与单词", b, end="")
for i in a:
    if i not in b:
        print("不", end="")
        break
else:
    for i in b:
        if i not in a:
            print("不", end="")
            break
print("是相似词")
