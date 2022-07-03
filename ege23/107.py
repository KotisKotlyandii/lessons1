a = [3]
for _ in range(7):
    b = []
    for i in a:
        b.append(i+1)
        b.append(i+4)
        b.append(i*2)
    a = b.copy()

print(a.count(27))