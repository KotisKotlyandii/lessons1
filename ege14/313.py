k = 0
for n in range(100000,10000000):
    if len(hex(n)[2:]) <= 8 and len(oct(n)[2:]) >= 11 and str(n)[-1] == '5':
        k += 1