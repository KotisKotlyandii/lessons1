import  sys

sys.stdin = open('24data/24-164.txt')

s = []
for _ in range(1000):
    s.append(input())

s = [i for i in s if i.count('G') < 15]
maxim = 0
for i in s:
    for n in i:
        tek = abs(i.index(n) - i.rindex(n))
        if tek > maxim:
            maxim = tek

print(maxim)