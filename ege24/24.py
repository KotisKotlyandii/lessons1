import sys
sys.stdin = open("24data/k7a-4.txt")

print(max(map(len, input().split("D"))))
