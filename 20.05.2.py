from random import randint
lent = int(input("Введите размер квадратной матрицы: "))
a, b = [], []
for i in range(lent):
    a.append([])
    b.append([])
    for j in range(lent):
        a[i].append(randint(0, 9))
        b[i].append(0)
for i in range(lent):
    for j in range(lent):
        b[i][j] = a[j][len(a)-1-i]

print("Матрица: ")
for i in range(lent):
    print(a[i])
print("Перевёрнутая матрица: ")
for i in range(lent):
    print(b[i])
