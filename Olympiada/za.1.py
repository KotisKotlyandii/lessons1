import sys  # импорт системный модуль sys

file = open(file="kodin.txt", mode="r")  # открываем файл kodin.txt для чтения read
file2 = open(file="kodout.txt", mode="w")  # откываем файл  kodout.txt для записи write
sys.stdin = file  # направляем поток ввода из файла file
sys.stdout = file2  # направляем поток вывода в файл file2

a = int(input())
b = int(input())
kol = 0
for number in range(100, 1000):
    if sum(map(int, str(number))) == a and number % b == 0:
        print(number)
        kol += 1
if kol == 0:
    print(0)
