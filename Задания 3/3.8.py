# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

screen_x = 900
screen_y = 650
sd.set_screen_size(screen_x, screen_y)
sd.background_color = sd.COLOR_BLACK
sd.caption = 'ScalesAir рисует Смайлы'


def smile(x, y):
    point = sd.get_point(x, y)
    color_smile = sd.random_color()
    color = sd.COLOR_BLACK
    # color = sd.random_color()
    # while color_smile == color:
    #     color = sd.random_color()
    sd.circle(point, radius=50, color=color_smile, width=0)
    eye_one = sd.get_point(x - 20, y + 15)
    eye_two = sd.get_point(x + 20, y + 15)
    mouth_x = sd.get_point(x - 20, y - 20)
    mouth_y = sd.get_point(x + 20, y - 20)
    mouth_z = sd.get_point(x, y - 30)
    sd.circle(eye_one, radius=2, color=color)
    sd.circle(eye_two, radius=2, color=color)
    sd.lines([mouth_x, mouth_z, mouth_y], color=color)


for _ in range(100):
    smile(sd.random_number(50, screen_x-50), sd.random_number(50, screen_y-50))
    sd.sleep(0.005)
sd.pause()
