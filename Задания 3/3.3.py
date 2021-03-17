# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
original_number = a
division_result = 0
# a, b = 4, 2
while a > b:
    a -= b
    division_result += 1

print('Целочисленное деление', original_number, 'на', b, 'дает', division_result)
