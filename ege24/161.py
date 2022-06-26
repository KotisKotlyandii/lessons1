import  sys

sys.stdin = open('24data/24-s1.txt')

s = []
for _ in range(1000):
    s.append(input())
nomer = []
for i in s:
    nomer.append(i.count("Q"))

naim_stroka = s[nomer.index(max(nomer))]
slovarik = {}
for i in naim_stroka:
    slovarik[i] = naim_stroka.count(i)

slovarik = {n:slovarik[n] for n in slovarik if slovarik[n] != 0}
max_str = min(slovarik.values())

bykv = min([i for i in slovarik if slovarik[i] == max_str])
kol = sum([i.count(bykv) for i in s])
print(bykv, kol)