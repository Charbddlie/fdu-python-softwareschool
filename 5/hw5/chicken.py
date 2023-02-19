for i in range(21):
    for j in range(34):
        k = 100 - i - j
        res = 5 * i + 3 * j + k / 3
        if res < 100 or k % 3 != 0:
            continue
        elif res == 100 and i + j + k == 100:
            print("公鸡" + str(i) + "只，" + "母鸡" + str(j) + "只，" + "小鸡" + str(k) + "只")
            break
        else:
            break
