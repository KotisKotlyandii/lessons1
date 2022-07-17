slov = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
def opr(chislo):
    a = str(chislo)
    for i in range(len(a)-1):
        if slov[a[i]] % 2 == slov[a[i+1]] % 2:
            return False
    else:
        return True

sed = set()
k = 0
for chislo in range(100,10000000):
    if len(hex(chislo)[2:]) == 5 and opr(hex(chislo)[2:]) and len(set(hex(chislo)[2:])) == 5:
        sed.add(chislo)
        k += 1
        print(hex(chislo)[2:])

print(k,len(sed))