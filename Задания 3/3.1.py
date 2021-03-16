# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)


def name_month(number_month):
    if 1 <= number_month <= 12:
        if number_month == 2:
            return '28 дней'
        elif number_month == 4:
            return '30 дней'
        elif number_month == 6:
            return '30 дней'
        elif number_month == 9:
            return '30 дней'
        elif number_month == 11:
            return '30 дней'
        else:
            return '31 день'
    else:
        return 'Вы ввели некорретный номер месяца'


print(name_month(month))
