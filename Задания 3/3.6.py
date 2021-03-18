# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.background_color = [0, 100, 255]
sd.caption = 'ScalesAir рисует радугу'
sd.set_screen_size(500, 500)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)


start_y = 50
end_y = 450
for color in rainbow_colors:
    start_point = sd.get_point(50, start_y)
    end_point = sd.get_point(350, end_y)
    sd.line(start_point, end_point, color, 4)
    start_y += 5
    end_y += 5


sd.sleep(5)
sd.clear_screen()

# sd.background_color = sd.COLOR_BLUE

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
start_x = 500
start_y = -200
radius = 540
for color in rainbow_colors:
    start_point = sd.get_point(start_x, start_y)
    sd.circle(start_point, radius=radius, color=color, width=20)
    radius -= 20

sd.sleep(5)
sd.pause()
sd.quit()
