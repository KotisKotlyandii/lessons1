def f(n):
    if n == 39:
        return 63245986
    if n == 40:
        return 102334155
    if n == 0:
        return 0
    if 0 < n < 3:
        return 1
    else:
        return f(n-2) + f(n-1)

def vuchisl_chils(n):
    poryadok = 1
    pos4chift = ""
    while poryadok != 5:
        pos4chift += str(n%10)
        n = n // 10
        poryadok += 1
    return pos4chift[::-1]

print(vuchisl_chils(f(47)))