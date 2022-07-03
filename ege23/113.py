a = [1]
kol = 0
while a.count(227) == 0:
    b = []
    for i in a:
        b.append(i+1)
        b.append(i+5)
        b.append(i*3)
    a = b.copy()
    kol += 1
print(kol)