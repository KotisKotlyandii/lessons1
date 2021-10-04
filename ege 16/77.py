def f(n):
    if n <= 1:
        return n
    if n > 1 and n % 3 == 0:
        return n + f(n/3)
    else:
        return n + f(n+3)

def vychisl_na_chislo(n):
    while True:
        if n == 1:
            return True
        if n % 3 == 0:
            n = n +
        else:
            return  False

for n in range(3,1001,3):

