# -*- coding: utf-8 -*-

import simple_draw as sd
sd.set_screen_size(800, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


def snowflakes(x, y, snow_length=10):
    while True:
        sd.start_drawing()
        _point = sd.get_point(x, y)
        sd.snowflake(center=_point, length=snow_length, color=sd.background_color)
        y -= 7
        _point = sd.get_point(x, y)
        sd.snowflake(center=_point, length=snow_length, color=sd.COLOR_WHITE)
        sd.sleep(0.1)
        sd.finish_drawing()
        if y < snow_length * 2:
            break
        if sd.user_want_exit():
            break


for _ in range(1000):
    snow_x = sd.random_number(50, 750)
    snowflakes(snow_x, 650)
    sd.sleep(3)


sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
