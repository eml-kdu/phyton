#Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

print('отображение элементов списка v_def_lis')
v_def_lis = [1, 'наименование', 'продукт 1', 3.43, 6, True]
v_def_lis.append(4)
v_def_lis.append('артикл')
v_last_index = v_def_lis.index('артикл')
v_current_index = 0
while v_current_index <= v_last_index:
    print(str(v_def_lis[v_current_index]) + ' тип значения ' + str((type(v_def_lis[v_current_index]))))
    v_current_index += 1


