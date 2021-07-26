def func(s):
    n = 4
    while s <= 96:
        s = s +8
        n = n + 5
    return n

k = 1
min = 0
max = 0

for s in range(1,1000):
    if func(s) == 54:
        if k == 1:
            min = s
            k += 1
        max = s

print(str(min)+str(max))