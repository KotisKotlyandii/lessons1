def f(n):
    if n < 2:
        return 2
    if n % 3 == 0:
        return f(n//3) + 1
    else:
        return f(n-2) + 5

for n in range(1,10001):
    if f(n) == 73:
        print(n)
        break

        