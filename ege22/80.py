def f(x):
    L = x - 18
    M = x + 36
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    return M

for x in range(101,10000):
    if f(x) == 9:
        print(x)
        break