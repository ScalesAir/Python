# -*- coding: utf-8 -*-

import simple_draw as sd

sd.set_screen_size(900, 600)
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


def triangle(point, angle=0, length=100, clear=0):
    """"" 
    Эта функция рисует треугольник 
    Принимает параметры: 
        next_point - Начальную точку рисования
        angle - угол наклона (по умолчанию 0)
        length - длина линий (по умолчанию 100)
        clear - очищаеть ли фигуру (0=белый цвет, 1=цвет фона)
    """""
    next_point = point
    for _ in range(3):
        v1 = sd.get_vector(start_point=next_point, angle=angle, length=length, width=3)
        next_point = v1.end_point
        angle += 120
        v1.draw(color=colors(clear))


def square(point, angle=0, length=100, clear=0):
    """"" 
    Эта функция рисует квадрат
    Принимает параметры: 
        next_point - Начальную точку рисования
        angle - угол наклона (по умолчанию 0)
        length - длина линий (по умолчанию 100)
        clear - очищаеть ли фигуру (0=белый цвет, 1=цвет фона)
    """""
    next_point = point
    for _ in range(4):
        v1 = sd.get_vector(start_point=next_point, angle=angle, length=length, width=3)
        next_point = v1.end_point
        angle += 90
        v1.draw(color=colors(clear))


def pentagon(point, angle=0, length=100, clear=0):
    """"" 
    Эта функция рисует пятиугольник
    Принимает параметры: 
        next_point - Начальную точку рисования
        angle - угол наклона (по умолчанию 0)
        length - длина линий (по умолчанию 100)
        clear - очищаеть ли фигуру (0=белый цвет, 1=цвет фона)
    """""
    next_point = point
    for _ in range(5):
        v1 = sd.get_vector(start_point=next_point, angle=angle, length=length, width=3)
        next_point = v1.end_point
        angle += 72
        v1.draw(color=colors(clear))


def hexagon(point, angle=0, length=100, clear=0):
    """"" 
    Эта функция рисует шестиугольник
    Принимает параметры: 
        next_point - Начальную точку рисования
        angle - угол наклона (по умолчанию 0)
        length - длина линий (по умолчанию 100)
        clear - очищаеть ли фигуру (0=белый цвет, 1=цвет фона)
    """""
    next_point = point
    for _ in range(6):
        v1 = sd.get_vector(start_point=next_point, angle=angle, length=length, width=3)
        next_point = v1.end_point
        angle += 60
        v1.draw(color=colors(clear))


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
        v1.draw(color=colors(clear))


clear_figure = 0
angle_figure = sd.random_number(-90, 0)
for _ in range(2):
    point_triangle = sd.get_point(130, 300)
    triangle(point_triangle, clear=clear_figure, angle=angle_figure)
    sd.sleep(0.5)
    point_square = sd.get_point(240, 300)
    square(point_square, clear=clear_figure, angle=angle_figure)
    sd.sleep(0.5)
    point_pentagon = sd.get_point(390, 300)
    pentagon(point_pentagon, clear=clear_figure, angle=angle_figure)
    sd.sleep(0.5)
    point_hexagon = sd.get_point(580, 300)
    hexagon(point_hexagon, clear=clear_figure, angle=angle_figure)
    clear_figure = 1

sd.clear_screen()

clear_figure = 0
multi_figure_x = 130
correct = 0
for number_figure in range(3, 12, 1):
    number = number_figure
    if number_figure == 7:
        multi_figure_x = 130
        correct = 0
    if number_figure > 6:
        number -= 4
        clear_figure = 1
    point_multi_figure = sd.get_point(multi_figure_x, 300)
    multi_figure(figure=number, point=point_multi_figure, clear=clear_figure, angle=angle_figure)
    multi_figure_x += (120 + correct)
    correct += 33
    sd.sleep(0.3)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

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
