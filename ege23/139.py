def f(a,b):
    if int(a,2) == int(b,2):
        return 1
    elif int(a,2) < int(b,2):
        return 0
    if '1' in a[1:]:
        return f(bin(int(a,2) - 1)[2:], b) + f('1'+'0'*len(a[1:]),b)
    else:
        return f(bin(int(a,2) - 1)[2:], b)


print(f('1000000','1000'))