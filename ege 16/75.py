def f(n):
    if n <= 1:
        return n
    if n > 1 and n % 2 == 0:
        return 1 + f(n//2)
    else:
        return 1 + f(n+2)

kol_chikl = 1


while True:
    if f(2**kol_chikl) == 16:
        print(2**kol_chikl)
        break
    kol_chikl += 1