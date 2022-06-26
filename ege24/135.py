import  sys


sys.stdin = open('24data/24-j4.txt')

t = input()

t =t.replace('JBOSS','J')
t =t.replace('JBOSSJ','J')
t =t.replace('BOSSJ','J')
t =t.replace('BOSS','F')
print(t.count('F'))