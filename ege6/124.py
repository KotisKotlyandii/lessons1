def func(s):
    n = 1
    while s < 54:
        s = s + 7
        n = n * 3
    return n

k = 0

for s in range(1,1000):
    if func(s) == 243:
        k += 1

print(k)
