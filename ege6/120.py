def func(s):
    n = 1
    while s < 45:
        s =s+8
        n =n*3
    return n

k = 0

for d in range(1,1000):
    if func(d) > 243:
        k += 1

print(k)