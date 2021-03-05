# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение площади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
area = 3.1415926 * (radius ** 2)
float(area)
print(round(area, 4))


# Далее, пусть есть координаты точки
point = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

height = (point[0]**2 + point[1]**2) ** 0.5
# print("Расстояние до точки от начала координат равно %.4f" % height)
print(height < radius)

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
height = (point_2[0]**2 + point_2[1]**2) ** 0.5
# print("Расстояние до точки от начала координат равно %.4f" % height)
print(height < radius)

# Пример вывода на консоль:
#
# 77777.7777
# False
# False