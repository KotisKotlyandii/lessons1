def f(a,b):
    if a == b:
        return 1
    elif a > b:
        return 0
    elif a % 10 == 9 and len(str(a)) == 2:
        return f(a+1,b) + f(a+10,b)
    elif a % 10 != 9 and a // 10 != 9:
        return f(a+1,b) + f(a + 11, b)

print(f(26,49))