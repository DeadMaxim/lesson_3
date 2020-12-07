def my_func(var_1, var_2, var_3):
    if var_1 >= var_3 and var_2 >= var_3:
        return var_1 + var_2
    elif var_1 > var_2 and var_1 < var_3:
        return var_1 + var_3
    else:
        return var_2 + var_3


print(
    f'Сумма наибольших двух аргументов: {my_func(float(input("Укажите первое значение")), float(input("Укажите второе значение")), float(input("Укажите третье значение")))}')
