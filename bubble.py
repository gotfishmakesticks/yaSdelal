from random import randint
from time import time
start_time = time()
if __name__ == '__main__':
    list = []
    iters = int(input("Введите кол-во элементов массива > "))

    for i in range(iters):
        ran = randint(0, 100)
        list.append(ran)

    print("Ваш массив: " + str(list))

    for i in range(len(list) - 1, 1, -1):
        # print(f"I = {i}")
        for j in range(1, i):
            # print(f"J = {j}")
            # print(f"[{list[j-1]}], [{list[j]}]")
            if list[j - 1] > list[j]:
                # print(f"{list[j-1]} > {list[j]}")
                buff = list[j - 1]
                list[j - 1] = list[j]
                list[j] = buff
        for k in range(i, 1, -1):
            if list[k] < list[k - 1]:
                buff = list[k]
                list[k] = list[k - 1]
                list[k - 1] = buff
print("Отсортированный массив: " + str(list))
print("--- %s seconds ---" % (time.time() - start_time))