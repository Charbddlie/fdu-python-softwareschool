s = float(input("score: "))
s = int(s*10)
res = ""
if 900 <= s <= 1000:
    res = "A"
elif 850 <= s <= 899:
    res = "A-"
elif 820 <= s <= 849:
    res = "B+"
elif 780 <= s <= 819:
    res = "B"
elif 750 <= s <= 779:
    res = "B-"
elif 710 <= s <= 749:
    res = "C+"
elif 660 <= s <= 709:
    res = "C"
elif 620 <= s <= 659:
    res = "C-"
elif 600 <= s <= 619:
    res = "D"
elif 0 <= s <= 599:
    res = "F"
else:
    res = "Error!"
print(res)
