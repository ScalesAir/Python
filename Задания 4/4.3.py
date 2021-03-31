# -*- coding: utf-8 -*-

import simple_draw as sd

sd.set_screen_size(900, 600)

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def colors(color_id):
    """""
        Функция в зависимости от параметра color_id возвращает цвет
        0 - белый
        1 - цвет фона
        Нужна только для того чтобы в каждой функции рисования фигур не сравнивать чему равен 
        передоваемый ей параметр clear и в зависимости от значения выбирать нужный цвет 
    """""
    color = sd.COLOR_WHITE
    if color_id == 1:
        color = sd.background_color

    return color


def multi_figure(figure, point, angle=0, length=100, clear=0):
    """"" 
    Эта функция рисует фигуру в зависимости от параметра figure
    Принимает параметры: 
        figure - фигура (triangle, square, pentagon, hexagon)
        next_point - Начальную точку рисования
        angle - угол наклона (по умолчанию 0)
        length - длина линий (по умолчанию 100)
        clear - очищаеть ли фигуру (0=белый цвет, 1=цвет фона)
    """""
    if (figure == 'triangle') or (figure == 1):
        _angle_figure = 120
        _Corners_figure = 3
    elif (figure == 'square') or (figure == 2):
        _angle_figure = 90
        _Corners_figure = 4
    elif (figure == 'pentagon') or (figure == 3):
        _angle_figure = 72
        _Corners_figure = 5
    elif (figure == 'hexagon') or (figure == 4):
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
        v1.draw(color=colors(clear))


text = "Список фигур:\n"
text += "Треугольник - 1\n"
text += "Квадрат - 2\n"
text += "Пятиугольник - 3\n"
text += "Шестиугольник - 4\n"
text += "Введите цифру нужной фигуры"
number = int(input(text))

if 0 < number < 5:
    point_multi_figure = sd.get_point(400, 280)
    multi_figure(figure=number, point=point_multi_figure)
else:
    print("Вы облажались!")

sd.pause()
