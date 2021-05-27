# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    step = abs(y)
    res = x
    while step > 1:
        res = res * x
        step -= 1

    if type(y) == int and y < 0:
        res = 1/res
    elif type(y) == int and y == 0:
        res = 0
    return res


try:
    x = float(input('Введите действительное положительное число x'))
    y = int(input('целое отрицательное число y'))
    if y > 0:
        print('Мы просили отрицательно ;-)  ')
        print('Результат до коррекции Y ' + str(my_func(x, y)))
        y = -1 * y
        print('Результат после коррекции Y ' + str(my_func(x, y)))
        print(str(my_func(x, y)))
    else:
        print('Результат Y ' + str(my_func(x, y)))
except Exception as e:
     error_log = str(e)
     print(error_log)


