def f1(s):
    return s + s[::-1] 


def f2(s):
    half = len(s) // 2
    for i in range(half):
        if not s[i] == s[len(s) - 1 - i]:
            return False
    return True

