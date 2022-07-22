kol_nom = int(input())
izn = list(input())
kon = list(input())
k = 0
for i in range(len(izn)):
    k += min(abs(int(izn[i]) - int(kon[i])),10 - abs(int(izn[i]) - int(kon[i])) )
print(k)