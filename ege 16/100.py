def f(n):
    if n == 30:
        return  243
    if n == 29:
        return  448
    if n <= 3:
        return n + 3
    if f(n-1) % 2 == 0:
        return  f(n-2) + n
    else:
        return f(n-2) + 2 * n

symma = 0

for n in range(40,51):
    symma += f(n)

print(symma)
