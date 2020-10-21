# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

ALL_COLOR = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

def common_part(start_point,angle,length,color, kol_povt):
    for _ in range(kol_povt):
        start_point = sd.vector(start=start_point, angle=angle, length=length, color = color)
        angle += 360/kol_povt


def triangle(*args):
    common_part(*args,3)


def square(*args):
    common_part(*args,4)


def pentagon(*args):
    common_part(*args,5)


def hexagon(*args):
    common_part(*args,6)


a = int(input("""Какой цвет вы хотите выбрать?
0 - Красный
1 - Оранжевый
2 - Желтый
3 - Зеленый
4 - Голубой
5 - Синий
6 - Пурпурный 
Выберите желаемый цвет > """))
while True:
    if  0 < a < 7:
        break
    else:
        print("Вы ввели некоректное число")
        a = int(input('Выберите желаемый цвет >'))
        continue
triangle(sd.Point(100, 100), 30, 100, ALL_COLOR[a])
square(sd.Point(370, 100), 30, 100, ALL_COLOR[a])
pentagon(sd.Point(150, 400), 30, 100, ALL_COLOR[a])
hexagon(sd.Point(450, 350), 30, 100, ALL_COLOR[a])
sd.pause()
