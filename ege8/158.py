def opr(chislo):
    a = str(chislo)
    for i in range(len(a)-1):
        if int(a[i]) % 2 == int(a[i+1]) % 2:
            return False
    else:
        return True
k = 0
for chislo in range(1000000,10000000):
    if chislo % 5 == 0 and len(set(str(chislo))) == 7 and opr(chislo):
        k += 1
        print(chislo)

print(k)