# import  sys
#
#
# sys.stdin = open('26data/26-k6.txt')

kol,nysh = map(int,input().split())

ves_chena = {}
for _ in range(kol):
    ves,chena = map(int,input().split())
    ves_chena[ves] = chena

ves_chena = {i:ves_chena[y]/i for i in ves_chena for y in ves_chena}
print(ves_chena)