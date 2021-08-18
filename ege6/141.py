def func(s):
    n = 1
    while s>n:
        s = s -15
        n = n * 5
    return n

k = 0

for s in range(-100,1000):
    if func(s) == 125:
        k += 1

print(k)
