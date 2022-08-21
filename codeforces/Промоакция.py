tovar,prov = map(int,input().split())
spis_tov = list(map(int,input().split()))

for _ in range(prov):
    x,y = map(int,input().split())
    b = spis_tov.copy()
    b.sort(reverse=True)
    for _ in range(len(b)-x):
        b.pop()
    print(sum(b[:x]))
