# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as s
from random import randint
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def smile(x, y, color):
    radius = 50
    s.circle(center_position=s.Point(x, y), radius=radius, color=color, width=0)
    s.circle(center_position=s.Point(x + 15, y + 20), radius=7, color=s.COLOR_CYAN, width=0)
    s.circle(center_position=s.Point(x - 15, y + 20), radius=7, color= s.COLOR_CYAN, width= 0)
    s.line(start_point=s.Point(x - 20, y - 10), end_point=s.Point(x + 20, y - 10), color=s.COLOR_RED, width = 4)
    s.line(start_point=s.Point(x -20 , y - 12), end_point=s.Point(x + -30, y + 5 ), color=s.COLOR_RED, width= 4)
    s.line(start_point=s.Point(x + 20, y - 12), end_point=s.Point(x + 30, y + 5), color=s.COLOR_RED, width=4)
for _ in range(10):
    smile(s.randint(0,600), s.randint(0,600), s.COLOR_YELLOW)
s.pause()

s.pause()
