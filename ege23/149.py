a = [3]
for _ in range(12):
    b = set()
    for i in a:
        b.add(i+1)
        b.add(i*2-3)
    a = b.copy()

print(len(a))