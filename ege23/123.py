kol = 0
for c in range(100):
    a = [c]
    for _ in range(5):
        b = []
        for i in a:
            b.append(i+1)
            b.append(i*2)
            b.append(i + i % 4)
        a = b.copy()
        if a.count(80) > 0:
            kol += 1

print(kol)