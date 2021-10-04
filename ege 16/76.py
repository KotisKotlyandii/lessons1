def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return 3 + f(n//2 - 1)
    else:
        return n + f(n+2)

def vychisl_na_chislo(n):
    while True:
        if n == 1:
            return True
        if n % 2 == 0:
            n = 3 + n // 2 - 1
        else:
            return  False

for n in range(1,1000):
    if vychisl_na_chislo(n):
        if f(n) == 19:
            print(n)
            break

