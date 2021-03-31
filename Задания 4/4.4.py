# -*- coding: utf-8 -*-

import simple_draw as sd
sd.set_screen_size(1100, 600)
sd.caption = "ScalesAir рисует дерево"

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# def draw_bunches(start_point, angle=90, length=100):
#     _angle_v1 = 90
#     _angle_v2 = _angle_v1
#     _length = length
#     _point_v1 = start_point
#     _point_v2 = start_point
#     v1 = sd.get_vector(start_point=start_point, angle=90, length=(length*3), width=2)
#     v1.draw(color=sd.COLOR_WHITE)
#     for _ in range(4):
#         v1 = sd.get_vector(start_point=_point_v1, angle=_angle_v1, length=_length, width=2)
#         v2 = sd.get_vector(start_point=_point_v2, angle=_angle_v2, length=_length, width=2)
#         v1.draw(color=sd.COLOR_WHITE)
#         v2.draw(color=sd.COLOR_WHITE)
#         _point_v1 = v1.end_point
#         _point_v2 = v2.end_point
#         _angle_v1 -= angle
#         _angle_v2 += angle
#         _length -= 30

def draw_bunches(start_point, angle=90, length=200, delta=30):
    if length < 1:
        return
    random_length = sd.random_number(-int(length * .50), int(length * .50))
    random_angel = sd.random_number(-7, 7)
    v1 = sd.get_vector(start_point=start_point, angle=angle+random_angel, length=length+random_length, width=2)
    v1.draw(color=sd.COLOR_WHITE)
    random_length = sd.random_number(-int(length * .50), int(length * .50))
    v2 = sd.get_vector(start_point=start_point, angle=angle+random_angel, length=length+random_length, width=2)
    v2.draw(color=sd.COLOR_WHITE)
    next_point_v1 = v1.end_point
    next_point_v2 = v2.end_point
    next_angle_v1 = angle + delta
    next_angle_v2 = angle - delta
    next_length_v1 = int(length * .75)
    next_length_v2 = int(length * .75)
    draw_bunches(start_point=next_point_v1, angle=next_angle_v1, length=next_length_v1, delta=delta)
    draw_bunches(start_point=next_point_v2, angle=next_angle_v2, length=next_length_v2, delta=delta)


point_tree = sd.get_point(550, -40)
draw_bunches(start_point=point_tree, angle=90, delta=30, length=150)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
