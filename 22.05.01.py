lent = int(input("Введите длину списка: "))
lookfor = int(input(f"Введите искомое число, оно не должно быть больше {lent+lent}: "))
answers = []
if lookfor <= lent+lent:
    for i in range(1, lent + 1):
        for j in range(1, lent + 1):
            if i+j==lookfor:
                answers.append(f"{i} и {j}")
    print("Ответ:\n"+str(answers))
else:
    print(f"Искомое число ({lookfor}) невозможно получить из чисел заданного диапазона (1-{lent})")