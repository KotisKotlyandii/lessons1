def chet(a):
    b = ''
    while a > 0:
        b += str(a % 4)
        a //= 4
    return b[::-1]
def f(a,b):
    if int(a,4) == int(b,4):
        return 1
    elif int(a,4) > int(b,4):
        return 0
    return f(chet(int(a,4) + 2), b) + f(chet(int(a,4) + 3)[2:], b) + f(a+'0',b)

print(f('1','100'))