def func(s):
    n = 11
    while s < 224:
        s = s +15
        n = n +8
    return n

for s in range(1,1000):
    if func(s) == 115:
        print(s)
        break
