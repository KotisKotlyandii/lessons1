a = [2]
for _ in range(7):
    b = []
    for i in a:
        b.append(i+1)
        b.append(i+3)
        b.append(i*2)
    a = b.copy()

print(a.count(25))