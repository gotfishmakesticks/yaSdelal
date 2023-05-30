ls = []
lent = int(input("Введите кол-во чисел в массиве: "))
lookfor = int(input("Введите искомое число: "))
left = 0
right = lent-1
iters = 1
returnable = -1
if 1 <= lookfor <= lent:
    while returnable < 0:
        mid = round((left + right) / 2)
        if lookfor == mid:
            print(f"Найдено число {lookfor} за {iters} итераций.")
            exit()
        elif lookfor > mid:
            left = mid + 1
        elif lookfor < mid:
            right = mid - 1
        iters += 1
