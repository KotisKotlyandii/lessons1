import sys

sys.stdin = open('24data/24-5.txt')


t = input()

t = t.replace('()','l')
print(t.count('l'))