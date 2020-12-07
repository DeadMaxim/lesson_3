stop_word = 0
sum_res = 0


def my_func(func_str):
    global stop_word
    my_list = func_str.split(' ')
    result = 0
    for i in range(len(my_list)):
        if my_list[i] == 'stop':
            stop_word = 1
            break
        else:
            counter = float(my_list[i])
            result = result + counter
    return result


print('Введите строку чисел, разделенных пробелом. Для завершения работы программы введите "Stop"')
while True:
    if stop_word == 1:
        print(f'Окончательный результат: {sum_res}')
        break
    else:
        my_str = input("введите строку: ")
        sum_res = sum_res + my_func(my_str)
        print(sum_res)
