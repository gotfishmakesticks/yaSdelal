list = []

for i in range(int(input("Введите размерность списка: "))):
    list.append([])

for i in range(len(list)):
    for j in range(len(list)):
        list[i].append(abs(i - j) + 1)

output = ""

for i in range(len(list)):
    for j in range(len(list[i])):
        output += f"{list[i][j]} "
    output += "\n"

print(output)