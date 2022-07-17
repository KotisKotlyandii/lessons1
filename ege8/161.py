def opr(chislo):
    a = str(chislo)
    for i in range(len(a)-1):
        if int(a[i]) % 2 == int(a[i+1]) % 2:
            return False
    else:
        return True
k = 0
for chislo in range(100,1000000):
    if len(oct(chislo)[2:]) == 6 and opr(oct(chislo)[2:]) and len(set(oct(chislo)[2:])) == 6:
        k += 1
        print(oct(chislo)[2:])

print(k)