def f(x):
    L = x - 30
    M = x + 30
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    return M

for x in range(101,10000):
    if f(x) == 15:
        print(x)
        break