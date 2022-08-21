tovar,prov = map(int,input().split())
a = list(map(int,input().split()))
x = []
y = []
for _ in range(prov):
    b, c = map(int,input().split())
    x.append(b)
    y.append(c)
m = max(x)
a2 = []
for i in range(m):
    t = a.index(max(a))
    a2.append(a.pop(t))
for i in range(prov):
    z = a2[:x[i]]
    print(sum(z[-y[i]:]))