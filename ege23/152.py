def f(a,b):
    if a == b:
        return 1
    elif a > b:
        return  0
    return  f(a+1,b) + f(a+2,b)

c1 = f(11,17)*f(17,29)
c2 = f(11,23)*f(23,29)
c3 = f(11,17)*f(17,23)*f(23,29)
print (c1+c2-c3)