def my_func(num_1, num_2):
    return num_1 / num_2


while True:
    var_1 = float(input('Укажите делимое: '))
    var_2 = float(input('Укажите делитель: '))
    if var_2 != 0:
        print(my_func(var_1, var_2))
        break
    else:
        print('Деление на ноль невозможно!')
