import sys

sys.stdin = open('26data/26-j7.txt')

k = int(input())

bog = int(k*0.2)
p = []
for _ in range(k):
    p.append(int(input()))
n = int(sum(p)*0.6)
b = []
for _ in range(bog):
    b.append(max(p))
    p.remove(max(p))
itog = int(sum(b)*0.8)
proc_s_bed = 0
for i in range(1,101):
    if itog + int((sum(p) * (i/100))) >= n:
                  proc_s_bed = i/100
                  break
print(itog,int(min(p)*proc_s_bed))
