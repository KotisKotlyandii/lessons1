def f(i):
    a = '1' * i
    while '111' in a:
        a = a.replace('111','2',1)
        a = a.replace('222','1',1)
    return a
for i in range(31,40):
    if f(i) == '211':
        print(i)
        break