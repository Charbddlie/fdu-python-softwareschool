# 当时做的时候网站有bug看不到网址，做法差不多，就是需要按网站里面的对应方式
words = ["春风", "匆匆", "多情", "江南", "相思", "归去", "为谁", "依旧", "憔悴", "回首"]
nums = input("请输入一串数字")
poetry = ""
for i in nums:
    try:
        poetry += words[int(i)]
    except:
        print("输入存在不是数字的字符")
        exit()

print(poetry)
