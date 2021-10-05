def f(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return f(n-1) + f(n-2)
    else:
        return 1.5*f(n-1)

list = []
len_f = int(f(15))
for poryadok in range(0, len(str(len_f))):
    list.append(str(len_f)[poryadok])

print(len(set(list)))