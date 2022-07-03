a = [2]
for _ in range(15):
    b = set()
    for i in a:
        b.add(i+2)
        b.add(i*2+1)
    a = b.copy()

print(len(a))