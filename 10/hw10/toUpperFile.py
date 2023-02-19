try:
    s1 = open("sample1.txt","r")
    s2 = open("sample2.txt","w")
except IOError:
    print("文件打开失败")
    exit()

while l := s1.readline():
    s2.write(l.upper())

s1.close()
s2.close()