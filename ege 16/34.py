def f(n):
    if n > 0:
        d = (n%10 + f(n//10))
        return  d
    else:
        return 0


print(f(520))
