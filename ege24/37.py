import sys
sys.stdin = open("24data/k7c-5.txt")

s = input()
k = 0
for i in range(len(s)-4):
    s2 = s[i:i+5]
    if s2[0] != s2[1] != s2[2] != s2[3] != s2[4]:
        k += 1
print(k)