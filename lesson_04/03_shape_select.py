# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
def triangle(*args):
    common_part(*args,3)


def square(*args):
    common_part(*args,4)


def pentagon(*args):
    common_part(*args,5)


def hexagon(*args):
    common_part(*args,6)


def common_part(start_point,angle,length, kol_povt):
    for _ in range(kol_povt):
        start_point = sd.vector(start=start_point, angle=angle, length=length)
        angle += 360/kol_povt


a = int(input("""Возможные фигуры:
0 - треугольник 
1 - квадрат 
2 - пятиугольник 
3 - шестиугольник
Введите желаемую фигуру > """))
while True:
    if -1 < a < 4:
        break
    else:
        print("Введено некоректное число!")
        a = int(input("Введите желаему фигуру > "))
        continue
if a == 0:
    triangle(sd.Point(370, 100), 30, 100)
if a == 1:
    square(sd.Point(370, 100), 30, 100)
if a == 2:
    pentagon(sd.Point(150, 400), 30, 100, )
if a == 3:
    hexagon(sd.Point(150, 400), 30, 100, )
sd.pause()