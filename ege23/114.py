a = [1]
while a.count(28) == 0:
    b = []
    for i in a:
        b.append(i+1)
        b.append(i+2)
        b.append(i*2)
    a = b.copy()
print(a.count(28))