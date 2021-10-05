def f(n):
    if n <= 5:
        return n
    if n % 5 == 0:
        return n + f(n//5+1)
    else:
        return n+f(n+6)

max = 0

def vychisl_na_chislo(n):
    while True:
        if n <= 5:
            return True
        if n % 5 == 0:
            n = n // 5 + 1
        else:
            return  False

for n in range(1,100000000):
    if vychisl_na_chislo(n):
        max = f(n)

print(max)