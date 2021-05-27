#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#и возвращает сумму наибольших двух аргументов.

def my_func(var_1, var_2, var_3):
    v_def_list = [var_1+var_2, var_1 + var_3, var_2 + var_3]
    res = max(v_def_list)
    print(str(res))
    return str(res)


print('Сумма наибольших двух аргументов  ' + my_func(1,32,1))
