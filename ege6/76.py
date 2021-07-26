def func(s):
    n = 105
    while n > s:
        s = s+3
        n = n -2
    return(n)

max = 0

for s in range(1,1000):
    if func(s) == 67:
        max = s

print(max)