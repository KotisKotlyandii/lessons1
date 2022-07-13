def f(x):
    L = x - 21
    M = x + 12
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    return M

for x in range(101,10000):
    if f(x) == 11:
        print(x)
        break