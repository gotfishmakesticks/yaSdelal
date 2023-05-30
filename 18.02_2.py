from random import random, randint
list = [-1000 + random() * 2000 for i in range(randint(1, 100))]
list.append(-1000)

positives = []
negatives = []

posSum = 0
negSum = 0

print(list)

for i in range(len(list)):
    if list[i] > 0:
        positives.append(list[i])
    elif list[i] < 0:
        negatives.append(list[i])
    else:
        positives.append(list[i])
        negatives.append(list[i])

for num in positives:
    posSum += num

for num in negatives:
    negSum += num

posAr = posSum / len(positives)
negAr = negSum / len(negatives)

print(f"Ответ:\nСумма положительных чисел: {posSum}\nСумма отрицательных чисел: {negSum}\nСреднее арифметическое положительных чисел: {posAr}\nСреднее арифметическое отрицательных чисел: {negAr}")