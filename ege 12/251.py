def f(i):
    a = '1' * i
    while '111' in a:
        a = a.replace('111','2',1)
        a = a.replace('2222','1',1)
    return a

for i in range(81,100):
    if f(i).count('1') == 0:
        print(i)
        break