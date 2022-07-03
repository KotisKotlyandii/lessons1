def f(a,b):
    if a == b:
        return 1
    elif a > b:
        return 0
    return f(a+1,b) + f(a+5,b) + f(a*3,b)

k = 0
while f(1,k) != 175: k += 1
print(k)