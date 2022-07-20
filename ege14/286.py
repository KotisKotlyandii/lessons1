for x in range(2,10000):
    a = 4 ** 2015 + 2 ** x - 2 ** 2015 + 15
    if bin(a).count('1') == 500:
        print(x)