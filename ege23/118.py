a = [1]
for _ in range(6):
    b = set()
    for i in a:
        b.add(i+1)
        b.add(i+2)
        b.add(i*2)
    a = b.copy()

print(len([i for i in a if i in range(34,60)]))