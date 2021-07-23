def func(s):
    n = 0
    while s <= 275:
        s = s + 5
        n = n + 2
    return n

for s in range(-1000,1000):
    if func(s) < 195:
        k = s
print(k)