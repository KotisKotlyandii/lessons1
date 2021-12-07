def prost(chislo):
    k = 0
    for i in range(2, chislo // 2 + 1):
        if (chislo % i == 0):
            k = k + 1
    if (k == 0):
        return  True
    else:
        return  False

spis = []

for chislo in range()