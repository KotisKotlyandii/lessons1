# -*- coding: utf-8 -*-

import simple_draw as sd
import pygame


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# def triangle(start_point, angle=0, length=100):
#     for _ in range(3):
#         start_point = sd.vector(start=start_point, angle=angle, length=length)
#         angle += 120
#
#
# def square(start_point, angle=0, length=100):
#     for _ in range(4):
#         start_point = sd.vector(start=start_point, angle=angle, length=length)
#         angle += 90
#
#
# def pentagon(start_point, angle=0, length=100):
#     for _ in range(5):
#         start_point = sd.vector(start=start_point, angle=angle, length=length)
#         angle += 72
#
#
# def hexagon(start_point, angle=0, length=100):
#     for _ in range(6):
#         start_point = sd.vector(start=start_point, angle=angle, length=length)
#         angle += 60


# point_0 = sd.get_point(200,200)
# hexagon(start_point=point_0)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

def common_part(start_point,angle,length,kol_povt):
    for _ in range(kol_povt):
        start_point = sd.vector(start=start_point, angle=angle, length=length)
        angle += 360/kol_povt


def triangle(*args):
    common_part(*args,3)


def square(*args):
    common_part(*args,4)


def pentagon(*args):
    common_part(*args,5)


def hexagon(*args):
    common_part(*args,6)


triangle(sd.Point(100, 100), 30, 100)
square(sd.Point(370, 100), 30, 100)
pentagon(sd.Point(150, 400), 30, 100)
hexagon(sd.Point(450, 350), 30, 100)


# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
