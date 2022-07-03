a = [1]
while a.count(111) == 0:
    b = []
    for i in a:
        b.append(i+1)
        b.append(i+5)
        b.append(i*3)
    a = b.copy()
print(a.count(111))