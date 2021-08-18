def func(s):
    n = 600
    while n > s:
        s = s + 3
        n = n - 6
    return n

k = 1
min = 0
max = 0

for s in range(1,1000):
    if func(s) == 210:
        if k == 1:
            min = s
            k += 1
        max = s

print(str(max)+str(min))