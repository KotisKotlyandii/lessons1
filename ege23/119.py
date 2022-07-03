a = [1]
for _ in range(8):
    b = set()
    for i in a:
        b.add(i+1)
        b.add(i+5)
        b.add(i*3)
    a = b.copy()

print(len([i for i in a if i in range(1000,1024+1)]))