import sys

sys.stdin = open('24data/k7b-2.txt')

t = input()

t1 = "DBAC"

while t1 in t:
    t1 += "DBAC"

if t1[:-1] in t:
    print(len(t1)-1)
elif t1[:-2] in t:
    print(len(t1)-2)
elif t1[:-3] in t:
    print(len(t1)-3)