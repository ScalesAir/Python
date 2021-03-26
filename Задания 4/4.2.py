# -*- coding: utf-8 -*-

import simple_draw as sd

sd.set_screen_size(900, 600)

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

colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]


def multi_figure(figure, point, angle=0, length=100, color_figure=sd.COLOR_WHITE):
    """"" 
    Эта функция рисует фигуру в зависимости от параметра figure
    Принимает параметры: 
        figure - фигура (triangle, square, pentagon, hexagon)
        next_point - Начальную точку рисования
        angle - угол наклона (по умолчанию 0)
        length - длина линий (по умолчанию 100)
        color - цвет фигуры
    """""
    if (figure == 'triangle') or (figure == 3):
        _angle_figure = 120
        _Corners_figure = 3
    elif (figure == 'square') or (figure == 4):
        _angle_figure = 90
        _Corners_figure = 4
    elif (figure == 'pentagon') or (figure == 5):
        _angle_figure = 72
        _Corners_figure = 5
    elif (figure == 'hexagon') or (figure == 6):
        _angle_figure = 60
        _Corners_figure = 6
    else:
        _angle_figure = 120
        _Corners_figure = 3
    next_point = point
    for _ in range(_Corners_figure):
        v1 = sd.get_vector(start_point=next_point, angle=angle, length=length, width=3)
        next_point = v1.end_point
        angle += _angle_figure
        v1.draw(color=color_figure)


text = "Укажите цвет фигур, где\n"
text += "1 - Красный\n"
text += "2 - Оранжевый\n"
text += "3 - Желтый\n"
text += "4 - Зеленый\n"
text += "5 - Голубой\n"
text += "6 - Синий\n"
text += "7 - Пурпурный\n"
user_color = int(input(text))

sd.clear_screen()
sd.sleep(3)
angle_figure = sd.random_number(-90, 0)
multi_figure_x = 130
correct = 0
color = colors[user_color-1]
for number_figure in range(3, 12, 1):
    number = number_figure
    if number_figure == 7:
        multi_figure_x = 130
        correct = 0
        sd.sleep(3)
    if number_figure > 6:
        number -= 4
        clear_figure = 1
        color = sd.background_color
    point_multi_figure = sd.get_point(multi_figure_x, 300)
    multi_figure(figure=number, point=point_multi_figure, angle=angle_figure, color_figure=color)
    multi_figure_x += (120 + correct)
    correct += 33
    sd.sleep(0.3)

sd.pause()
