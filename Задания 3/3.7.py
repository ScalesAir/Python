# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# Длина холста
screen_size_x = 830
# Высота холста
screen_size_y = 620
simple_draw.set_screen_size(screen_size_x, screen_size_y)
simple_draw.caption = "ScalesAir рисует стену"
simple_draw.background_color = simple_draw.COLOR_ORANGE

left_y = 0
top_y = 50
bias = 0
left_x = -50
count_brick_x = (screen_size_x / 100) + 1
count_brick_y = (screen_size_y / 50) + 1
for _ in range(round(count_brick_y)):
    if bias == 0:
        left_x = 0
        top_x = 100
        bias = 1
    else:
        left_x = -50
        top_x = 50
        bias = 0
    for _ in range(round(count_brick_x)):
        left = simple_draw.get_point(left_x, left_y)
        top = simple_draw.get_point(top_x, top_y)
        simple_draw.rectangle(left, top, simple_draw.COLOR_DARK_ORANGE, width=2)
        left_x += 100
        top_x += 100
        simple_draw.sleep(0.05)

    left_y += 50
    top_y += 50
    top_x += 50

simple_draw.pause()
