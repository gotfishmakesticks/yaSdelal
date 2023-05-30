list = []

for i in range(int(input("Введите размерность списка (нечётное число!): "))):
    list.append([])

mid = ((len(list) + 1) / 2) - 1

for i in range(len(list)):
    for j in range(len(list)):
        list[i].append(".")

for i in range(len(list)):
    for j in range(len(list)):
        if i == j or i == len(list) - j - 1 or i == mid or j == mid:
            list[i][j] = "*"

output = ""

for i in range(len(list)):
    for j in range(len(list[i])):
        output += f"{list[i][j]} "
    output += "\n"

print(output)