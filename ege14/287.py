for x in range(2,10000):
    a = 4 ** 1014 - 2 ** x + 12
    if bin(a).count('0') - 1 == 2000:
        print(x)