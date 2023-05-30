from random import randint
list = [randint(-100, 100) for i in range(randint(1, 100))]

print(list)

unique = True

for i in range(len(list)):
    for j in range(i + 1, len(list) - 1):
        if list[i] == list[j]:
            unique = False
            break

if unique:
    print("Все числа списка уникальны.")
else:
    print("В списке есть совпадения.")