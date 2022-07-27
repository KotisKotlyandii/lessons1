def f(a):
    r = 0
    if a.count(0) == len(a):
        return 0
    for i in range(len(a)):
        if a[i] != 0:
            r = i
            break
    return a[r:-1].count(0) + sum(a[:-1])


for _ in range(int(input())):
    k = int(input())
    a = list(map(int,input().split()))
    print(f(a))