def f(n):
    s = ''
    while n > 0:
        s = str(n%5) + s
        n //= 5
    return s
k = 0
for n in range(10,18):
    k += f(n).count('2')
print(k)