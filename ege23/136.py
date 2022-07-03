def f(a,b):
    if int(a,2) == int(b,2):
        return 1
    elif int(a,2) > int(b,2):
        return 0
    return f(bin(int(a,2) + 1)[2:], b) + f('1'+a,b)

print(f('1','11111'))