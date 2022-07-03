a = [1]
for _ in range(8):
    b = []
    for i in a:
        b.append(i+1)
        b.append(i*2)
        b.append(i*3)
    a = b.copy()

print(a.count(34))