a = [1]
for _ in range(4):
    b = set()
    for i in a:
        b.add(i+1)
        b.add(i+5)
        b.add(i*3)
    a = b.copy()

print(len(a))