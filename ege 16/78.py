def f(n):
    if n <= 1:
        return n
    if n % 3 == 0:
        return n + f(n//3-1)
    else:
        return n+f(n+3)

def vychisl_na_chislo(n):
    while True:
        if n <= 1:
            return True
        if n % 3 == 0:
            n = n // 3 - 1
        else:
            return  False

for n in range(1,10001):
    if vychisl_na_chislo(n):
        if f(n) > 1000:
            print(n)
            break