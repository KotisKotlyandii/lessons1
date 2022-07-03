a = [3]
for _ in range(11):
    b = set()
    for i in a:
        b.add(i+1)
        b.add(i*2+1)
    a = b.copy()

print(len(a))