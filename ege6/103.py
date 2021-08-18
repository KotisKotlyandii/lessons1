def func(s):
    n = 5
    while n > 0:
        s = s + n
        n = n - 1
    return s

max = 0

for s in range(1,1000):
    if func(s) <= 550:
        max = s

print(max)