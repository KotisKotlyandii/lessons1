import sys
sys.stdin = open("24data/24-169.txt ")

s = input()
i = 0
s1 = "XYZ"
while s1 in s:
    i += 1
    s1 = "XYZ" * i
print(i)
print(23*"XYZ" in s)
print(22*"XYZ"+"X" in s)
print("Z"+22*"XYZ" in s)
print("Z"+22*"XYZ"+"X" in s)
print("YZ"+22*"XYZ"+"X" in s, len("YZ"+22*"XYZ"+"X"))
print("YZ"+22*"XYZ"+"XY" in s)
print("XYZ"+22*"XYZ"+"X" in s)