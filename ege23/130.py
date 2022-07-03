a = [10]
for _ in range(5):
    b = set()
    for i in a:
        b.add(i+2)
        b.add(i+3)
        b.add(i*2)
    a = b.copy()

print(a)
print(len(a))