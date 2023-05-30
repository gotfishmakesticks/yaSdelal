lexa = {1: 12, 2: 24, 3: "Ярик"}

for k, v in lexa.items():
    print(k, v)
    lexa[k] = int(input('Ввод: '))
    print(k, lexa[k])