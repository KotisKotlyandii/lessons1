def f(x):
    L = x - 16
    M = x + 16
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    return M

for x in range(101,10000):
    if f(x) == 16:
        print(x)
        break