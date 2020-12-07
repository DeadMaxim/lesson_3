def my_func(x, y):
    rand_num = x
    for i in range(-1, y, -1):
        rand_num = rand_num * x
    result = 1 / rand_num
    return result


def another_func(var_1, var_2):
    rand_list = []
    for i in range(0, var_2, -1):
        rand_list.append(var_1)
    rand_num = rand_list[0]
    for i in range(len(rand_list) - 1):
        rand_num = rand_num * var_1
    result = 1 / rand_num
    return result


while True:
    x = float(input('Укажите вещественное положительное число: '))
    y = int(input('Укажите целое отрицательное число: '))
    if x > 0 and y < 0:
        print(f'Результат: {my_func(x, y)}')
        print(f'Ещё один вариант: {another_func(x, y)}')
        break
    else:
        print('Внимательно прочитайте условия задачи')
