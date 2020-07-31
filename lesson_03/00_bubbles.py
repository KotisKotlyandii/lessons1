# -*- coding: utf-8 -*-

import simple_draw as sd
import random
sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(100,100)
# radius = 50
# for _ in range(3):
#    radius += 5
#    sd.circle(center_position=point, radius= radius)
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color = color,  width=2)


# point = sd.get_point(300, 300)

# Нарисовать 10 пузырьков в ряд
# for x in range(100 , 1100 , 100):
#    point = sd.get_point(x, 100)
#    bubble(point = point, step = 1)
# Нарисовать три ряда по 10 пузырьков
# for y in range(100 , 400 , 100):
#    for x in range(100, 1100, 100):
#        point = sd.get_point(x, y)
#        bubble(point = point, step = 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    step = random.randint(2,10)
    bubble(point=point, step = step , color = color )

sd.pause()