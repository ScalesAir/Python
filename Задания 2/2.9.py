# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продукты следующего вида (писать прямо в коде)
sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'магнит', 'price': 11.99},
    ],
    'конфеты': [
        {'shop': 'ашан', 'price': 34.99},
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99},
    ],
    'карамель': [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'пятерочка', 'price': 46.99},
        {'shop': 'магнит', 'price': 41.99},
    ],
    'пирожное': [
        {'shop': 'ашан', 'price': 67.99},
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ],
}
shop = shops['ашан']
ashan = round(shop[0]["price"] + shop[1]["price"] + shop[0]["price"], 2)
shop = shops['пятерочка']
pyaterochka = round(shop[0]["price"] + shop[1]["price"] + shop[0]["price"], 2)
shop = shops['магнит']
magnit = round(shop[0]["price"] + shop[1]["price"] + shop[0]["price"], 2)

print('Cумма товаров Ашан -', ashan)
print('Cумма товаров Пятерочка -', pyaterochka)
print('Cумма товаров Магнит -', magnit)

# Указать надо только по 2 магазина с минимальными ценами
shops_min_price = {
        'печенье': [
            {'shop': 'ашан', 'price': 10.99},
            {'shop': 'пятерочка', 'price': 9.99},
        ],
        'конфеты': [
            {'shop': 'пятерочка', 'price': 32.99},
            {'shop': 'магнит', 'price': 30.99},
        ],
        'карамель': [
            {'shop': 'ашан', 'price': 45.99},
            {'shop': 'магнит', 'price': 41.99},
        ],
        'пирожное': [
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.99},
        ],
    }
print("\n\n")
shop = shops_min_price['печенье']
print('Печенье -', shop[0]['shop'], "и", shop[1]['shop'])
shop = shops_min_price['конфеты']
print('Конфеты -', shop[0]['shop'], "и", shop[1]['shop'])
shop = shops_min_price['карамель']
print('Карамель -', shop[0]['shop'], "и", shop[1]['shop'])
shop = shops_min_price['пирожное']
print('Пирожное -', shop[0]['shop'], "и", shop[1]['shop'])