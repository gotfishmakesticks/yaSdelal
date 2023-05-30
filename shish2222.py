

state = 0
loop = 0
while state != -1:
    if state == 0:
        print("Введите операцию\n+ - Сложить введённые числа\n- - Вычесть из первого числа остальные\n* - Умножить все введённые числа\n/ - Разделить первое число на остальные\nsquare - Решить квадратное уравнение\nquit - Завершить программу")
        loop = 1
        while loop == 1:
            inp = input()
            if inp == "quit":
                state = -1
                loop = 0
            elif inp == "+":
                state = 1
                loop = 0
            elif inp == "-":
                state = 2
                loop = 0
            elif inp == "*":
                state = 3
                loop = 0
            elif inp == "/":
                state = 4
                loop = 0
            elif inp == "square":
                state = 5
                loop = 0
            else:
                print("Неверный ввод")
    elif state == 1:
        print("Сложение чисел. Вводите числа, чтобы получить результат, введите 0, чтобы выйти в меню, можно дроби")
        sum = 0
        loop = 1
        while loop == 1:
            inp = float(input())
            if inp == 0:
                loop = 0
                state = 0
            sum += inp
            print(str(sum-inp) + " + " + str(inp) + " = " + str(sum))
