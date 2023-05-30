def binary(lf, left, right, iters):
    mid = round((left + right) / 2)
    if lf == mid:
        return f"Найдено число {lf} за {iters} итераций."
    elif lf > mid:
        return binary(lf, mid + 1, right, iters + 1)
    elif lf < mid:
        return binary(lf, left, mid - 1, iters + 1)

print(binary(int(input("Введите искомое число: ")), 1, int(input("Введите кол-во чисел в массиве: ")), 1))