def func(s):
    n = 0
    while 400 < s*s:
        s = s - 1
        n = n + 3
    return n

max = 0

for s in range(1,1000):
    if func(s) < 1000:
        max = s

print(max)