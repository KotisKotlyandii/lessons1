import sys

sys.stdin = open('24data/k7b-5.txt')

t = input()

t1 = "CA"

while t1 in t:
    t1 += "CA"

if t1[:-1] in t:
    print(len(t1)-1)
else:
    print(len(t1))