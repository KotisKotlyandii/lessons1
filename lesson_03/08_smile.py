# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as s
from random import randint
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def head(x,y,color):
    s.ellipse(left_bottom=x, right_top=y, color = color)
for _ in range(10):
    head(x = s.random_point(), y = s.random_point(), color=s.random_color())


s.pause()
