a = [1]
for _ in range(15):
    b = set()
    for i in a:
        b.add(i+3)
        b.add(i*3)
    a = b.copy()

b = [i for i in a if i % 2 == 0 and i < 100]
print(b)
print(len(b))