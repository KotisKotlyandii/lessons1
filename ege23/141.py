def tri(a):
    b = ''
    while a > 0:
        b += str(a%3)
        a //= 3
    return b[::-1]

def f(a,b):
    if int(a,3) == int(b,3):
        return 1
    elif int(a,3) < int(b,3):
        return 0
    if a[-1] == 0:
        return f(tri(int(a,3) - 2),b)
    else:
        return f(tri(int(a,3) - 2),b) + f(a[:-1] + '0',b)

print(f('212','10'))