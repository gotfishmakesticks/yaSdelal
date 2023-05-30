from random import randint
def func1(context):
    ls = context.split(' ', 2)
    km = 0
    match(ls[1]):
        case 'км':
            km = float(ls[0])
        case 'м':
            km = float(ls[0])/1000
        case 'см':
            km = float(ls[0])/100000
        case 'мм':
            km = float(ls[0])/1000000
    m = km * 1000
    cm = km * 100000
    mm = km * 1000000
    print(f'Это {mm} мм, {cm} см, {m} м, {km} км')


def func2(context):
    dict = {
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре',
        '5': 'пять',
        '6': 'шесть',
        '7': 'семь',
        '8': 'восемь',
        '9': 'девять',
        '10': 'десять',
        '11': 'одиннадцать',
        '12': 'двенадцать',
        '13': 'тринадцать',
        '14': 'четырнадцать',
        '15': 'пятнадцать',
        '16': 'шестнадцать',
        '17': 'семнадцать',
        '18': 'восемнадцать',
        '19': 'девятнадцать',
        '20': 'двадцать',
        '30': 'тридцать',
        '40': 'сорок',
        '50': 'пятьдесят',
        '60': 'шестьдесят',
        '70': 'семьдесят',
        '80': 'восемьдесят',
        '90': 'девяносто',
    }
    ls = context.split(' ', 2)
    if len(ls[1]) == 2 and ls[1][0] != '1':
        ls.append(ls[1][0] + '0')
        ls[1] = dict[ls[2]] + ' ' +dict[ls[1][1]]
    else:
        ls[1] = dict[ls[1]]
    print(f'Вас зовут {ls[0]} и вам {ls[1]} лет. Это занимает {len(ls[0] + ls[1])} символов.')


def chess(context):
    ls = context.split(' ', 4)
    if ls[0] == ls[2] and ls[1] == ls[3]:
        print('Вы пытаетесь попасть в ту же клетку, в которой уже находится король.')
        return
    for i in range(len(ls)):
        ls[i] = int(ls[i])
    if ls[0] - 1 <= ls[2] <= ls[0] + 1 and ls[1] - 1 <= ls[3] <= ls[1] + 1:
        print('Король может попасть во вторую клетку за 1 ход.')
    else:
        print('Король не может попасть во вторую клетку за 1 ход.')


def listappender(context):
    l,t,r = [],[],[]
    for i in range(int(context)): l.append(randint(-128, 128))
    for i in range(int(context)): t.append(randint(-128, 128))
    print('1 список:', l)
    print('2 список:', t)
    for i in range(int(context)):
        r.append(l[i])
        r.append(t[i])
    print(r)


def calculation(context):
    ls = context.split(' ', 2)
    ls[0] = int(ls[0])
    ls[1] = int(ls[1])
    sum = ls[0] + ls[1]
    dev = ls[0] - ls[1]
    print(f'Сумма: {ls[0]} + {ls[1]} = {sum}\nРазность: {ls[0]} - {ls[1]} = {dev}')


func1(input('Введите длину, например 10 см: '))
func2(input('Введите имя и возраст, например Аня 2: '))
chess(input('Введите 4 числа от 1 до 8, отвечающие за клетки на шахматной доске (например 1 2 2 2): '))
listappender(input('Введите длину списков: '))
calculation(input('Введите 2 числа: '))