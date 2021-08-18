def func(s):
    n = 10
    while s-n < 1000:
        s = s + n
        n = n + 5
    return n

k = 0

for s in range(1,1000):
    if func(s) == 80:
        k += 1

print(k)