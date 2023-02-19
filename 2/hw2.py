# 产生1个0~99的列表
a = list(range(0, 100))

# 你能写出几种让列表元素逆序排列的方法（结果仍存放在a中）？答案写在下面。
a.sort(reverse=True)
a = sorted(a, reverse=True)
a = reversed(a)
a = a[100::-1]
a = [a[i] for i in range(99, -1, -1)]

# 重新排序
a.sort()
# 利用切片得到a中从21开始的所有奇数,存放在列表b中。答案写在下面。
b = a[21::2]

# 利用列表推导式，得到a中所有的质数,存放在列表c中。答案写在下面。


def is_prime(i):
    for j in range(2, i//2+1):
        if i % j == 0:
            return False
    return True


c = [i for i in a[2:] if is_prime(i)]

# 利用列表推导式，得到a中所有能被2或3整除的数,存放在列表d中。答案写在下面。
d = [i for i in a[2:] if i % 3 == 0 or i % 2 == 0]
