def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return f(n//2) + 3
    else:
        return 2 * f(n-1) + 1

list = []

for n in range(1,1001):
        list.append(f(n))

print(len(set(list)))
