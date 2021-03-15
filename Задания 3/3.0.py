# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = [0, 0, 0]
sd.caption = 'ScalesAir рисует кружки :)'

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(150, 150)
# radius = 50
# for _ in range(100, 400, 100):
#     radius += 20
#     sd.circle(center_position=point, radius=radius, color=[250, 100, 87], width=5)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# def bubble(point, step=2, width=2):
def bubble(coordinates_x=150, coordinates_y=150, width=2, random_color=0):
    point = sd.get_point(coordinates_x, coordinates_y)
    radius = 50
    if random_color:
        color = sd.random_color()
    else:
        color = [255, 255, 0]
    step = 7
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=width, color=color)


# point = sd.get_point(150, 150)
# bubble(point, 10)

# Нарисовать 10 пузырьков в ряд
# for x in range(150, 1101, 100):
#     bubble(x, 300, 2)

# Нарисовать три ряда по 10 пузырьков
# for y in range(200, 500, 100):
#     for x in range(150, 1101, 100):
#         bubble(x, y, 2)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    x = random.randint(100, 1100)
    y = random.randint(100, 500)
    bubble(x, y, random_color=1)

sd.pause()
