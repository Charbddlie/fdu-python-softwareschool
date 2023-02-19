import re
email = input("请输入email字符串")
res = re.match(r".*@.*[..*]*",email)
print(True if not res == None else False)