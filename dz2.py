a, b = int(input("Введите a: ")), int(input("Введите b: "))
print("---------------------------\n|Выберите действие:       |\n|1 - Сложение             |\n|2 - Вычитание            |\n|3 - Умножение            |\n|4 - Деление              |\n|5 - Решение кв. уравнения|\n---------------------------\n")
inp = int(input())
if inp == 1:
    print("Результат: " + str(a + b))
if inp == 2:
    print("Результат: " + str(a - b))
if inp == 3:
    print("Результат: " + str(a * b))
if inp == 4:
    print("Результат: " + str(a / b))
if inp == 5:
    c = int(input("a =" + str(a) + ", b = " + str(b) + ", c = "))
    d = b * b - (4 * a * c)
    if d < 0:
        print("Дискриминант отрицательный, все ответы представлены в комплексной плоскости.")
    print("d = " + str(d) + ", x1 = " + str((-b + d ** 0.5)/(2 * a)) + ", x2 = " + str((-b - d ** 0.5)/(2 * a)))
if inp > 5 or inp < 1:
    print("В следующий раз повезёт!")