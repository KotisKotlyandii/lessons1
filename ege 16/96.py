def f(n):
    if n < 10:
        return n
    if n >= 10:
        return n % 10 + f(n//10)

def g(n):
    if n < 10:
        return n
    if n >= 10:
        return g(f(n))

symma = 0

for n in range(10,100):
    symma += g(n)

print(symma)