import sys

sys.stdin = open("17 (2).txt")
masiv = []
vtor = list()
for i in range(5001):
    masiv.append(int(input()))
maxim = 0
kol = 0
for i in range(0,len(masiv)-1,2):
    perv = masiv[i]
    vtor = masiv[i+1]
    if (perv+vtor) % 2 == 0 and (perv+vtor) % 10 != 6:
        kol += 1
        maxim = max(maxim,(perv+vtor) // 2)

print(kol,maxim)