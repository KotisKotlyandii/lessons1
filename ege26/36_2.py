import sys

sys.stdin = open('26data/26-j8.txt')

k = int(input())
tov = []
for _ in range(k):
    tov.append(int(input()))
tov.sort()
print(k)
print(tov)
s1 = sum(tov[:7000])*0.7+sum(tov[7000:])*0.6
s2 = sum(tov[:5000])*0.6+sum(tov[5000:])*0.65
print(s1-s2)
print(max(tov[:7000])*0.7,max(tov[7000:])*0.6)