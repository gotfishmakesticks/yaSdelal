from random import randint
list = []
i = 1
while i != 0:
    i = randint(-10, 10)
    list.append(i)

posSign = True
switches = 0

print(list)

for i in range(len(list)):
    if list[i] > 0 and posSign == False:
        posSign = True
        switches += 1
    if list[i] < 0 and posSign == True:
        posSign = False
        switches += 1

print(f"Ответ:\nЗнак поменялся {switches} раз.")