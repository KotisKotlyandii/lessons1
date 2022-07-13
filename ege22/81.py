def f(x):
    L = x - 20
    M = x + 15
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    return M

for x in range(101,10000):
    if f(x) == 35:
        print(x)
        break