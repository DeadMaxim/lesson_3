def my_func(var_1, var_2):
    result = var_1 ** var_2
    return result


while True:
    x = float(input('Укажите вещественное положительное число: '))
    y = int(input('Укажите целое отрицательное число: '))
    if x > 0 and y < 0:
        print(f'Результат: {my_func(x, y)}')
        break
    else:
        print('Внимательно прочитайте условия задачи')
