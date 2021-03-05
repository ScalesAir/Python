# -*- coding: utf-8 -*-

# Создайте списки:
# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Я', 'Отец', 'Мать', 'Сестра', 'Брат', 'Дедушка', 'Бабушка']
# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], 189],
    [my_family[1], 191],
    [my_family[2], 173],
    [my_family[3], 154],
    [my_family[4], 167],
    [my_family[5], 182],
    [my_family[6], 175]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца', my_family_height[1][1], 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
overall_growth = my_family_height[0][1] + \
                 my_family_height[1][1] + \
                 my_family_height[2][1] + \
                 my_family_height[3][1] + \
                 my_family_height[4][1] + \
                 my_family_height[5][1] + \
                 my_family_height[6][1]
print('Общий рост моей семьи -', overall_growth, 'см')