1.
a = int(input())
b = int(input())
kol = 0
for number in range(100,1000):
        if number%10+number//100+(number//10) % 10 == a and number % b == 0:
                print(number)
                kol += 1
if kol == 0:
        print(0)