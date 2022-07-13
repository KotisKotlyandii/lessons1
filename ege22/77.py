def f(x):
    L = x - 12
    M = x + 12
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    return M

for x in range(101,10000):
    if f(x) == 2:
        print(x)
        break